# -*- coding:utf-8 -*-
import torch
import numpy as np
import pandas as pd
from torch.utils.data import TensorDataset
from sklearn.preprocessing import MinMaxScaler


class StandardScaler(object):
    def __init__(self):
        self.mean = 0.
        self.std = 1.

    def fit_transform(self, data):
        self.mean = data.mean(0)
        self.std = data.std(0)

    def transform(self, data):
        mean = torch.from_numpy(self.mean).type_as(data).to(data.device) if torch.is_tensor(data) else self.mean
        std = torch.from_numpy(self.std).type_as(data).to(data.device) if torch.is_tensor(data) else self.std
        return (data - mean) / std

    def inverse_transform(self, data):
        mean = torch.from_numpy(self.mean).type_as(data).to(data.device) if torch.is_tensor(data) else self.mean
        std = torch.from_numpy(self.std).type_as(data).to(data.device) if torch.is_tensor(data) else self.std
        return (data * std.values) + mean.values


class DataProcess(object):
    def __init__(self, window=144, predict_length=1, horizon=0, train_proportion=0.8, total_predict_length=600,
                 normalize='std'):
        self.window = window
        self.predict_length = predict_length
        self.horizon = horizon
        self.train_proportion = train_proportion
        self.total_predict_length = total_predict_length
        self.normalize = normalize
        self.scaler = StandardScaler()

    def normalized(self, data):

        # if self.normalize == 'min_max':
        #     self.scaler = MinMaxScaler()
        self.scaler.fit_transform(data)
        normalized_data = self.scaler.transform(data)
        return normalized_data

    def invert_normalized(self, data):
        invert_data = self.scaler.inverse_transform(data)
        return invert_data

    def train_test_split(self, data):
        # predict_input = []
        if self.normalize:
            data = self.normalized(data)
        train_valid_data = data.iloc[:-(self.window + self.horizon + self.total_predict_length), :]
        # predict_input.append(data.iloc[-(self.predict_length + self.window + self.horizon):-(self.predict_length + self.horizon), :].values.reshape(1, self.window, data.shape[1]))  # 验证集
        # if self.horizon == 0:
        #     predict_input.append(
        #         data.iloc[-(self.window + self.horizon):, :].values.reshape(1, self.window, data.shape[1]))  # 预测输入
        # else:
        #     predict_input.append(data.iloc[-(self.window + self.horizon): -self.horizon, :].values.reshape(1, self.window, data.shape[1]))  # 预测输入

        train_length = int(len(train_valid_data) * self.train_proportion)
        train_range = range(0, train_length + 1)
        train_input, train_label = self.batchify(train_range, data)

        valid_range = range(train_length + 1, len(train_valid_data) + 1)
        valid_input, valid_label = self.batchify(valid_range, data)

        test_data = data.iloc[-(self.window + self.horizon + self.total_predict_length):, :]

        return train_input, train_label, valid_input, valid_label, test_data

    def batchify(self, index_range=None, data=None):
        idx_set = index_range if index_range else len(data)
        data = data.values if isinstance(data, pd.DataFrame) else data
        dimension = data.shape[1]
        n = len(index_range) - self.window - self.horizon - self.predict_length
        input = np.zeros((n, self.window, dimension))
        target = np.zeros((n, self.predict_length, dimension))
        for index in range(n):
            x_start = idx_set[index]
            x_end = x_start + self.window
            y_start = x_end + self.horizon
            y_end = y_start + self.predict_length
            input[index, :, :] = data[x_start:x_end, :]
            target[index, :, :] = data[y_start:y_end, :]
        return input, target
