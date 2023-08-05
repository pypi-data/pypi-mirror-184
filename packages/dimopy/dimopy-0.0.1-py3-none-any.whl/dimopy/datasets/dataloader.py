"""
    pytorch dataset
"""
from numpy import float32
from torch.utils.data import DataLoader


class UnsupervisedLoader(object):
    def __init__(self, x_train, win_size, step=1):
        self.step = step
        self.win_size = win_size
        self.x_train = x_train

    def __len__(self):
        return (self.x_train.shape[0] - self.win_size) // self.step + 1

    def __getitem__(self, index: int):
        index = index * self.step
        return float32(self.x_train[index:index + self.win_size]), float32(self.x_train[index:index + self.win_size])


class SupervisedLoader(object):
    def __init__(self, x_train, y_train, win_size, step=1):
        self.step = step
        self.win_size = win_size
        self.x_train = x_train
        self.y_train = y_train

    def __len__(self):
        return (self.x_train.shape[0] - self.win_size) // self.step + 1

    def __getitem__(self, index: int):
        index = index * self.step
        return float32(self.x_train[index:index + self.win_size]), float32(self.y_train[index:index + self.win_size])


class ThresholdLoader(object):
    def __init__(self, x_train, y_train, win_size, step=1):
        self.step = step
        self.win_size = win_size
        self.x_train = x_train
        self.y_train = y_train

    def __len__(self):
        return (self.x_train.shape[0] - self.win_size) // self.win_size + 1

    def __getitem__(self, index: int):
        index = index * self.step
        return float32(self.x_train[
                       index // self.step * self.win_size:index // self.step * self.win_size + self.win_size]), float32(
            self.y_train[index // self.step * self.win_size:index // self.step * self.win_size + self.win_size])


def to_dataloader(x_train=None, y_train=None, batch_size=256, win_size=100, step=1,
                  shuffle: bool = True, mode='unsupervised'):
    if mode == 'unsupervised':
        dataset = UnsupervisedLoader(x_train=x_train, win_size=win_size, step=step)
    elif mode == 'supervised':
        dataset = SupervisedLoader(x_train=x_train, y_train=y_train, win_size=win_size, step=step)
    else:
        dataset = ThresholdLoader(x_train=x_train, y_train=y_train, win_size=win_size, step=step)

    data_loader = DataLoader(dataset=dataset,
                             batch_size=batch_size,
                             shuffle=shuffle,
                             num_workers=0)
    return data_loader
