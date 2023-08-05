# -*- coding:utf-8 -*-
import copy
import time

import pandas as pd
from sklearn.preprocessing import StandardScaler

'''
    数据归一化模块:
    z_score标准化
    min_max标准化
'''


class DataNormalization(object):

    def __init__(self, target=None, method='z_score', min=0, max=1):
        self.target = target
        self.method = method
        self.min = min
        self.max = max

    def z_score(self, data):
        self.standard = StandardScaler()
        data[self.target] = self.standard.fit_transform(data[self.target].values.reshape(-1, 1))
        return data

    def min_max(self, data):
        self.gap = self.max - self.min
        self.min_value = data[self.target].min()
        self.max_value = data[self.target].max()
        data[self.target] = data[self.target].apply(
            lambda x: self.min + ((x - self.min_value) / (self.max_value - self.min_value)) * self.gap)
        return data

    def standardization(self, data):
        start = time.time()
        if self.method == 'z_score':
            data = self.z_score(data)
        else:
            data = self.min_max(data)
        print('data standardization takes %s ' % (time.time() - start))
        return data

    def invert_standardized(self, df):
        start = time.time()
        if self.method == 'z_score':
            df[self.target] = self.standard.inverse_transform(df[self.target].values.reshape(-1, 1))
        else:
            df[self.target] = df[self.target].apply(
                lambda x: self.min_value + (x - self.min) * (self.max_value - self.min_value) / self.gap)
        print('data invert standardization takes %s ' % (time.time() - start))
        return df
