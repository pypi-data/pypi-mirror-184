# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from scipy.stats.mstats import winsorize


class DataOutlier(object):
    def __init__(self, method="", k=3, low_rate=0.025, up_rate=0.025):
        self.method = method
        self.k = k
        self.low_rate = low_rate
        self.up_rate = up_rate

    def mean_detect(self, data, p=0.05):
        """
        将偏离均值前1%的数据标记为nan
        @param data:
        @return:
        """

        diff_mean = (data[self.target] - data[self.target].mean()).abs()
        data.loc[diff_mean > diff_mean.quantile(1 - p), self.target] = np.nan
        return data

    def box_detect(self, data):
        Q1 = np.nanpercentile(data[self.target], 25)
        Q3 = np.nanpercentile(data[self.target], 75)
        IQR = Q3 - Q1
        index_list = data.loc[(data[self.target] < Q1 - 1.5 * IQR) | (data[self.target] > Q3 + 1.5 * IQR)].index
        return index_list

    def ksigma_detect(self, data):
        mean = np.nanmean(data[self.target])
        std = np.nanstd(data[self.target])
        upper = mean + self.k * std
        lower = mean - self.k * std
        index_list = data.loc[(data[self.target] < lower) | (data[self.target] > upper)].index
        return index_list

    def winsorize_detect(self, data):
        data[self.target] = winsorize(data[self.target], limits=(self.low_rate, self.up_rate))
        return data

    def outliers_processing(self, data):
        columns = data.columns.tolist()
        data.replace(to_replace=r'^\s*$', value=np.nan, regex=True, inplace=True)
        for col in columns:
            if 'time' in col:
                continue
            self.target = col
            if self.method == "box":
                idx_list = self.box_detect(data)
                data[self.target].iloc[idx_list] = np.nan
            elif self.method == "ksigma":
                idx_list = self.ksigma_detect(data)
                data[self.target].iloc[idx_list] = np.nan
            elif self.method == "winsorize":
                data = self.winsorize_detect(data)
            elif self.method == "mean":
                data = self.mean_detect(data, p=0.05)
        return data

