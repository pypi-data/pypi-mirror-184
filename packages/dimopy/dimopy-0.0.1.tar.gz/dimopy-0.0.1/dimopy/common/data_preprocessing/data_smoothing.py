# -*- coding:utf-8 -*-
import time
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
from tsmoothie.smoother import KalmanSmoother

'''
    数据平滑模块
    1. 窗口平滑；
    2. 卡尔曼滤波平滑
'''


class DataSmoothing(object):
    def __init__(self, target=None, method='windows_smooth', windows=10, periods=7):
        self.target = target
        self.method = method
        self.windows = windows
        self.periods = periods

    def windows_smooth(self, data):
        data[self.target] = data[self.target].rolling(window=self.windows, min_periods=1).mean()
        return data

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

        return start,end

    def kalman_smooth(self, data):
        data['time'] = pd.to_datetime(data['time'])
        self.granularity = self.get_granularity(data)
        start,end = self.get_effect_time(data)
        start_time = datetime.strptime(start, "%H:%M:%S")
        end_time = datetime.strptime(end, "%H:%M:%S")
        seconds = (end_time - start_time).seconds
        self.per_dayLen = seconds // self.granularity + 1
        self.periods = self.periods * self.per_dayLen
        smoother = KalmanSmoother(component='level_longseason',
                                  component_noise={'level': 0.1, 'longseason': 0.1},
                                  n_longseasons=self.periods, copy=False)
        smoother.smooth(data[[self.target]].T)
        data[self.target] = smoother.smooth_data[0]
        return data

    def smooth(self, data):
        start = time.time()
        if self.method == 'kalman':
            data = self.kalman_smooth(data)
        else:
            data = self.windows_smooth(data)
        print('data smoothing takes %s ' % (time.time() - start))
        return data
