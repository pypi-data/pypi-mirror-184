import torch
import torch.nn as nn
import time
import numpy as np
import os
from torch.backends import cudnn
from typing import Dict, Any
from dimopy.models.anomaly.lib.attn import AnomalyAttention, AttentionLayer
from dimopy.models.anomaly.lib.embed import DataEmbedding
from dimopy.models.anomaly.lib.encoder import Encoder, EncoderLayer
from dimopy.datasets.dataloader import to_dataloader
from dimopy.models.anomaly.lib.utils.utils import anomaly_kl_loss, adjust_learning_rate, EarlyStopping


class AnomalyModule(nn.Module):
    def __init__(self,
                 win_size: int,
                 enc_in: int,
                 c_out: int,
                 d_model: int = 512,
                 n_heads: int = 8,
                 e_layers: int = 3,
                 d_ff: int = 512,
                 dropout: float = 0.0,
                 activation: str = 'gelu',
                 output_attention: bool = True):
        super(AnomalyModule, self).__init__()
        self.output_attention = output_attention
        cudnn.benchmark = True
        # Encoding
        self.embedding = DataEmbedding(enc_in, d_model, dropout)

        # Encoder
        self.encoder = Encoder(
            [
                EncoderLayer(
                    AttentionLayer(
                        AnomalyAttention(win_size, False, attention_dropout=dropout, output_attention=output_attention),
                        d_model, n_heads),
                    d_model,
                    d_ff,
                    dropout=dropout,
                    activation=activation
                ) for l in range(e_layers)
            ],
            norm_layer=torch.nn.LayerNorm(d_model)
        )

        self.projection = nn.Linear(d_model, c_out, bias=True)

    def forward(self, x):
        enc_out = self.embedding(x)
        enc_out, series, prior, sigmas = self.encoder(enc_out)
        enc_out = self.projection(enc_out)

        if self.output_attention:
            return enc_out, series, prior, sigmas
        else:
            return enc_out  # [B, L, D]


class AnomalyTransformer(object):
    """
    Anomaly-Transformer (ICLR 2022 Spotlight)

    Unsupervised detection of anomaly points in time series is a challenging problem, which requires the model
    to learn informative representation and derive a distinguishable criterion.
    In this paper, we propose the Anomaly Transformer in these three folds:

    1. An inherent distinguishable criterion as Association Discrepancy for detection.
    2. A new Anomaly-Attention mechanism to compute the association discrepancy.
    3. A minimax strategy to amplify the normal-abnormal distinguishable of the association discrepancy.
    paper: https://arxiv.org/abs/2110.02642
    github: https://github.com/thuml/Anomaly-Transformer
    """

    def __init__(
            self,
            lr: float = 1e-4,
            num_epochs: int = 10,
            k: int = 3,
            win_size: int = 100,
            batch_size: int = 256,
            pretrained_model: str = None,
            model_save_path: str = 'checkpoints',
            anomaly_ratio: float = 4.0,
            step: int = 1,
            dataset: str = 'model'
    ):

        self.lr = lr
        self.num_epochs = num_epochs
        self.k = k
        self.win_size = win_size
        self.batch_size = batch_size
        self.pretrained_model = pretrained_model
        self.model_save_path = model_save_path
        self.anomaly_ratio = anomaly_ratio
        self.step = step
        self.dataset = dataset
        self.criterion = None
        self.device = None
        self._fit_params = None
        self.train_loader = None
        self.valid_loader = None
        self.test_loader = None
        self.thre_loader = None
        self.optimizer = None
        self.model = None

        super(AnomalyTransformer, self).__init__()

    def _update_fit_params(
            self,
            train_tsdataset
    ) -> Dict[str, Any]:
        self._fit_params = {
            "observed_dim": train_tsdataset.shape[1]}
        return self._fit_params

    def _init_fit_dataloaders(
            self,
            train_tsdataset,
            valid_tsdataset,
            shuffle: bool = True):
        """
            Generate dataloaders for train and eval set.
        """
        train_dataloader = to_dataloader(train_tsdataset, batch_size=self.batch_size, win_size=self.win_size,
                                         step=self.step, shuffle=shuffle, mode='unsupervised')

        valid_dataloaders = to_dataloader(valid_tsdataset, batch_size=self.batch_size, win_size=self.win_size,
                                          step=self.step, shuffle=False, mode='unsupervised')

        return train_dataloader, valid_dataloaders

    def _init_predict_dataloaders(
            self,
            test_tsdataset,
            test_tslabel,
            shuffle: bool = False):
        """
            Generate dataloaders for predict set.
        """
        test_dataloader = to_dataloader(x_train=test_tsdataset, y_train=test_tslabel, batch_size=self.batch_size,
                                        win_size=self.win_size, step=self.step, shuffle=shuffle, mode='supervised')

        return test_dataloader

    def _init_threshold_dataloaders(
            self,
            test_tsdataset,
            test_tslabel,
            shuffle: bool = False):
        """
            Generate dataloaders for predict set.
        """
        threshold_dataloader = to_dataloader(x_train=test_tsdataset, y_train=test_tslabel, batch_size=self.batch_size,
                                             win_size=self.win_size, step=self.step, shuffle=shuffle, mode='threshold')

        return threshold_dataloader

    def build_model(self):
        """
            build model
        """

        self.model = AnomalyModule(
            win_size=self.win_size,
            enc_in=self._fit_params["observed_dim"],
            c_out=self._fit_params["observed_dim"],
            d_model=512,
            n_heads=8,
            e_layers=3,
            d_ff=512,
            dropout=0.0,
            activation='gelu',
            output_attention=True
        )

        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=self.lr)

        if torch.cuda.is_available():
            self.model.cuda()

    def fit(self, train_tsdataset, valid_tsdataset=None, valid_split=0.75):
        """
            训练接口
        """
        self._update_fit_params(train_tsdataset)

        # 设置验证集
        if valid_tsdataset is None and valid_split > 0:
            train_len = int(train_tsdataset.shape[0] * valid_split)
            valid_tsdataset = train_tsdataset[train_len:, :]
            train_tsdataset = train_tsdataset[0:train_len, :]
        print(f'train: {train_tsdataset.shape}')
        print(f'valid: {valid_tsdataset.shape}')
        self.train_loader, self.valid_loader = self._init_fit_dataloaders(train_tsdataset, valid_tsdataset)
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.criterion = nn.MSELoss()

        # build_model
        self.build_model()

        # train
        self._fit()

    def _fit(self):
        self.train()

    def predict(self, test_tsdataset, test_tslabel):
        self.test_loader = self._init_predict_dataloaders(test_tsdataset, test_tslabel)
        self.thre_loader = self._init_threshold_dataloaders(test_tsdataset, test_tslabel)
        gt_label, pred_label = self.test()

        return gt_label, pred_label

    def vali(self, vali_loader):
        self.model.eval()

        loss_1 = []
        loss_2 = []
        for i, (input_data, _) in enumerate(vali_loader):
            input = input_data.float().to(self.device)
            output, series, prior, _ = self.model(input)
            series_loss = 0.0
            prior_loss = 0.0
            for u in range(len(prior)):
                series_loss += (torch.mean(anomaly_kl_loss(series[u], (
                        prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                               self.win_size)).detach())) + torch.mean(
                    anomaly_kl_loss(
                        (prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                self.win_size)).detach(),
                        series[u])))
                prior_loss += (torch.mean(
                    anomaly_kl_loss((prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                            self.win_size)),
                                    series[u].detach())) + torch.mean(
                    anomaly_kl_loss(series[u].detach(),
                                    (prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                            self.win_size)))))
            series_loss = series_loss / len(prior)
            prior_loss = prior_loss / len(prior)

            rec_loss = self.criterion(output, input)
            loss_1.append((rec_loss - self.k * series_loss).item())
            loss_2.append((rec_loss + self.k * prior_loss).item())

        return np.average(loss_1), np.average(loss_2)

    def train(self):

        time_now = time.time()
        path = self.model_save_path
        if not os.path.exists(path):
            os.makedirs(path)
        early_stopping = EarlyStopping(patience=3, verbose=True, dataset_name=self.dataset)
        train_steps = len(self.train_loader)

        for epoch in range(self.num_epochs):
            iter_count = 0
            loss1_list = []

            epoch_time = time.time()
            self.model.train()

            for i, (input_data, labels) in enumerate(self.train_loader):

                self.optimizer.zero_grad()
                iter_count += 1
                input = input_data.float().to(self.device)

                output, series, prior, _ = self.model(input)

                # calculate Association discrepancy
                series_loss = 0.0
                prior_loss = 0.0

                for u in range(len(prior)):
                    series_loss += (torch.mean(anomaly_kl_loss(series[u], (prior[u] / torch.unsqueeze(
                        torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1, self.win_size)).detach())) + torch.mean(
                        anomaly_kl_loss((prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(
                            1, 1, 1, self.win_size)).detach(), series[u])))
                    prior_loss += (torch.mean(anomaly_kl_loss(
                        (prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                self.win_size)),
                        series[u].detach())) + torch.mean(
                        anomaly_kl_loss(series[u].detach(), (
                                prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                       self.win_size)))))
                series_loss = series_loss / len(prior)
                prior_loss = prior_loss / len(prior)

                rec_loss = self.criterion(output, input)

                loss1_list.append((rec_loss - self.k * series_loss).item())
                loss1 = rec_loss - self.k * series_loss
                loss2 = rec_loss + self.k * prior_loss

                if (i + 1) % 100 == 0:
                    speed = (time.time() - time_now) / iter_count
                    left_time = speed * ((self.num_epochs - epoch) * train_steps - i)
                    print('\tspeed: {:.4f}s/iter; left time: {:.4f}s'.format(speed, left_time))
                    iter_count = 0
                    time_now = time.time()

                # Minimax strategy
                loss1.backward(retain_graph=True)
                loss2.backward()
                self.optimizer.step()

            print("Epoch: {} cost time: {}".format(epoch + 1, time.time() - epoch_time))
            train_loss = np.average(loss1_list)

            vali_loss1, vali_loss2 = self.vali(self.valid_loader)

            print(
                "Epoch: {0}, Steps: {1} | Train Loss: {2:.7f} Vali Loss: {3:.7f} ".format(
                    epoch + 1, train_steps, train_loss, vali_loss1))
            early_stopping(vali_loss1, vali_loss2, self.model, path)
            if early_stopping.early_stop:
                print("Early stopping")
                break
            adjust_learning_rate(self.optimizer, epoch + 1, self.lr)

    def test(self):
        self.model.load_state_dict(
            torch.load(os.path.join(str(self.model_save_path), str(self.dataset) + '_checkpoint.pth')))
        self.model.eval()
        temperature = 50

        criterion = nn.MSELoss(reduce=False)

        # (1) stastic on the train set
        attens_energy = []
        for i, (input_data, labels) in enumerate(self.train_loader):
            input = input_data.float().to(self.device)
            output, series, prior, _ = self.model(input)
            loss = torch.mean(criterion(input, output), dim=-1)
            series_loss = 0.0
            prior_loss = 0.0
            for u in range(len(prior)):
                if u == 0:
                    series_loss = anomaly_kl_loss(series[u], (
                            prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                   self.win_size)).detach()) * temperature
                    prior_loss = anomaly_kl_loss(
                        (prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                self.win_size)),
                        series[u].detach()) * temperature
                else:
                    series_loss += anomaly_kl_loss(series[u], (
                            prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                   self.win_size)).detach()) * temperature
                    prior_loss += anomaly_kl_loss(
                        (prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                self.win_size)),
                        series[u].detach()) * temperature

            metric = torch.softmax((-series_loss - prior_loss), dim=-1)
            cri = metric * loss
            cri = cri.detach().cpu().numpy()
            attens_energy.append(cri)

        attens_energy = np.concatenate(attens_energy, axis=0).reshape(-1)
        train_energy = np.array(attens_energy)

        # (2) find the threshold
        attens_energy = []
        for i, (input_data, labels) in enumerate(self.thre_loader):
            input = input_data.float().to(self.device)
            output, series, prior, _ = self.model(input)

            loss = torch.mean(criterion(input, output), dim=-1)

            series_loss = 0.0
            prior_loss = 0.0
            for u in range(len(prior)):
                if u == 0:
                    series_loss = anomaly_kl_loss(series[u], (
                            prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                   self.win_size)).detach()) * temperature
                    prior_loss = anomaly_kl_loss(
                        (prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                self.win_size)),
                        series[u].detach()) * temperature
                else:
                    series_loss += anomaly_kl_loss(series[u], (
                            prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                   self.win_size)).detach()) * temperature
                    prior_loss += anomaly_kl_loss(
                        (prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                self.win_size)),
                        series[u].detach()) * temperature
            # Metric
            metric = torch.softmax((-series_loss - prior_loss), dim=-1)
            cri = metric * loss
            cri = cri.detach().cpu().numpy()
            attens_energy.append(cri)

        attens_energy = np.concatenate(attens_energy, axis=0).reshape(-1)
        test_energy = np.array(attens_energy)
        combined_energy = np.concatenate([train_energy, test_energy], axis=0)
        thresh = np.percentile(combined_energy, 100 - self.anomaly_ratio)
        print("Threshold :", thresh)

        # (3) evaluation on the test set
        test_labels = []
        attens_energy = []
        for i, (input_data, labels) in enumerate(self.thre_loader):
            input = input_data.float().to(self.device)
            output, series, prior, _ = self.model(input)

            loss = torch.mean(criterion(input, output), dim=-1)

            series_loss = 0.0
            prior_loss = 0.0
            for u in range(len(prior)):
                if u == 0:
                    series_loss = anomaly_kl_loss(series[u], (
                            prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                   self.win_size)).detach()) * temperature
                    prior_loss = anomaly_kl_loss(
                        (prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                self.win_size)),
                        series[u].detach()) * temperature
                else:
                    series_loss += anomaly_kl_loss(series[u], (
                            prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                   self.win_size)).detach()) * temperature
                    prior_loss += anomaly_kl_loss(
                        (prior[u] / torch.unsqueeze(torch.sum(prior[u], dim=-1), dim=-1).repeat(1, 1, 1,
                                                                                                self.win_size)),
                        series[u].detach()) * temperature
            metric = torch.softmax((-series_loss - prior_loss), dim=-1)

            cri = metric * loss
            cri = cri.detach().cpu().numpy()
            attens_energy.append(cri)
            test_labels.append(labels)

        attens_energy = np.concatenate(attens_energy, axis=0).reshape(-1)
        test_labels = np.concatenate(test_labels, axis=0).reshape(-1)
        test_energy = np.array(attens_energy)
        test_labels = np.array(test_labels)

        pred = (test_energy > thresh).astype(int)

        gt = test_labels.astype(int)

        # detection adjustment
        anomaly_state = False
        for i in range(len(gt)):
            if gt[i] == 1 and pred[i] == 1 and not anomaly_state:
                anomaly_state = True
                for j in range(i, 0, -1):
                    if gt[j] == 0:
                        break
                    else:
                        if pred[j] == 0:
                            pred[j] = 1
                for j in range(i, len(gt)):
                    if gt[j] == 0:
                        break
                    else:
                        if pred[j] == 0:
                            pred[j] = 1
            elif gt[i] == 0:
                anomaly_state = False
            if anomaly_state:
                pred[i] = 1

        pred = np.array(pred)
        gt = np.array(gt)

        return gt, pred
