# -*- coding:utf-8 -*-
import time
from datetime import datetime

import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


class DataFilling(object):
    def __init__(self, method="", period=None, order=2, alpha=0.5):
        self.method = method
        self.periods = period
        self.order = order
        self.alpha = alpha

    def get_granularity(self, df):

        df['time'] = pd.to_datetime(df['time'])
        time_lag = df['time'].apply(lambda x: int(time.mktime(time.strptime(str(x), '%Y-%m-%d %H:%M:%S')))).diff()
        granularity = sorted(time_lag.mode().values)[-1]
        return int(granularity)

    def get_effect_time(self, df):
        start, end = set(), set()
        df['time'] = pd.to_datetime(df['time'])
        df = df.sort_values(by=['time'], ascending=True)
        df['date'] = df['time'].dt.date
        for date, group in df.groupby('date'):
            temp_start, temp_end = str(group['time'].iloc[0]).split()[1], str(group['time'].iloc[-1]).split()[1]
            start.add(temp_start)
            end.add(temp_end)
        start, end = sorted(list(start))[0], sorted(list(end))[-1]
        return start, end

    def window_mean_fill(self, data, window=1):
        for idx, value in data.iterrows():
            if np.isnan(value.value):
                data.loc[idx, self.target] = data.loc[idx - window:idx + window, self.target].mean()
        return data

    def backward_front_fill(self, data):
        data[self.target].fillna(method='bfill', inplace=True)
        data[self.target].fillna(method='ffill', inplace=True)
        data[self.target].dropna(inplace=True, axis=0)
        return data

    def mean_fill(self, data):
        mean_value = data[self.target].mean()
        data[self.target].fillna(mean_value, inplace=True)
        return data

    def median_fill(self, data):
        median_value = data[self.target].median()
        data[self.target].fillna(median_value, inplace=True)
        return data

    def mode_fill(self, data):
        mode_value = max(data[self.target].mode().values)
        data[self.target].fillna(mode_value, inplace=True)
        return data

    def linear_fill(self, data):
        '''线性插值'''
        data[self.target].interpolate(method='linear', inplace=True)
        data[self.target].dropna(axis=0, inplace=True)
        return data

    def quadratic_fill(self, data):
        '''2次插值'''
        data[self.target].interpolate(method='quadratic', inplace=True)
        data[self.target].dropna(axis=0, inplace=True)
        return data

    def cubic_fill(self, data):
        '''3次插值'''
        data[self.target].interpolate(method='cubic', inplace=True)
        data[self.target].dropna(axis=0, inplace=True)
        return data

    def spline_fill(self, data):
        '''3次样条插值'''
        data[self.target].interpolate(method='spline', order=3, inplace=True)
        data[self.target].dropna(axis=0, inplace=True)
        return data

    def polynomial_fill(self, data):
        data[self.target].interpolate(method='polynomial', order=self.order, inplace=True)
        data[self.target].dropna(axis=0, inplace=True)
        return data

    def period_fill(self, data, index, periods):
        temp_data = []
        raw_values = data[self.target][:index].values

        for i in range(periods):
            temp_index = -(i + 1) * self.periods * self.per_dayLen
            temp_data.append(raw_values[temp_index])

        return np.nanmedian(temp_data)

    def fit_fill(self, data, index):
        if index > len(self.train_data):
            self.train_data.extend(data[len(self.train_data):index][self.target].values.tolist())
        ets = ExponentialSmoothing(self.train_data, seasonal_periods=self.data_nums_per_periods)
        ets_model = ets.fit()
        ets_forecast = ets_model.forecast(1)
        # self.train_data.append(ets_forecast)
        return ets_forecast

    def filling(self, data):
        columns = data.columns.tolist()
        for col in columns:
            if not data[col].isnull().any() or 'time' in col:
                continue

            self.target = col
            if self.method == "bffill":
                data = self.backward_front_fill(data)
            elif self.method == "window":
                data = self.window_mean_fill(data, window=1)
            elif self.method == "mean":
                data = self.mean_fill(data)
            elif self.method == "median":
                data = self.median_fill(data)
            elif self.method == "mode":
                data = self.mode_fill(data)
            elif self.method == "linear":
                data = self.linear_fill(data)
            elif self.method == "cubic":
                data = self.cubic_fill(data)
            elif self.method == "spline":
                data = self.spline_fill(data)
            elif self.method == "quadratic":
                data = self.quadratic_fill(data)
            elif self.method == "polynomia":
                data = self.polynomial_fill(data)
            elif self.method == "periodically":
                data['time'] = pd.to_datetime(data['time'])
                self.granularity = self.get_granularity(data)
                start, end = self.get_effect_time(data)
                start_time = datetime.strptime(start, "%H:%M:%S")
                end_time = datetime.strptime(end, "%H:%M:%S")
                seconds = (end_time - start_time).seconds
                self.per_dayLen = seconds // self.granularity + 1
                self.data_nums_per_periods = self.periods * self.per_dayLen
                index_list = data.loc[data[self.target].isnull()].index
                self.train_data = data[:index_list[0]][self.target].values.tolist()

                for index in index_list:
                    periods = min(index // (self.data_nums_per_periods), 4)
                    if periods < 1:
                        data[:index + 1] = self.mean_fill(data[:index + 1])
                    else:
                        period_fill_value = self.period_fill(data, index, periods)
                        fit_fill_value = self.fit_fill(data, index)
                        data.loc[index, [self.target]] = self.alpha * period_fill_value + (
                                    1 - self.alpha) * fit_fill_value
        return data
