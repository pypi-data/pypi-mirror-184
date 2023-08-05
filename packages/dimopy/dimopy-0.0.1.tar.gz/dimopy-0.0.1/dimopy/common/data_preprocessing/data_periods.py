# -*- coding:utf-8 -*-
from datetime import timedelta

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.signal as signal
from scipy.fftpack import fft
from statsmodels.tsa.stattools import acf


class DataPeriods(object):

    def __init__(self, getPeriodMethod="fft", windows=30, granularity=60, perDayLen=1440):
        self.getPeriodMethod = getPeriodMethod
        self.windows = windows
        self.granularity = granularity
        self.perDayLen = perDayLen

    def smoother(self, data):
        df = pd.DataFrame({"value": data})
        df['value'] = df['value'].rolling(window=10, min_periods=1, center=False).mean()
        df.dropna(inplace=True)
        return df['value'].values

    def fft_periods(self, timeseries, n=10, fmin=0.02):
        '''
            # 功能：把函数进行傅里叶变换，变换到频域，以期获得函数的周期,需要完整5~10个周期
            # 输入：时间序列，获取频率点数值n（可选），频率对应幅度的下限值fmin（可选）
            # 输入序列的X轴需要归一化为1
            # 输出： n个序列的下标以及对应的幅度值
        '''
        period = None
        timeseries = self.smoother(timeseries)
        fftValue = abs(fft(timeseries))
        fftNorm = fftValue / len(timeseries)
        fftNorm = (fftNorm[range(int(len(timeseries) / 2))]) * 2  # 频率

        fwbest = fftNorm[signal.argrelextrema(fftNorm, np.greater)]  # 频率对应的极大值
        xwbest = signal.argrelextrema(fftNorm, np.greater)[0]  # 频率极大值对应的索引
        xorder = np.argsort(-fwbest)  # 对获取到的极值进行降序排序，也就是频率越接近，越排前

        freq, ffts = [], []
        for index in xorder[:n]:
            if fwbest[index] >= fmin:
                freq.append(xwbest[index])
                ffts.append(fwbest[index])
        periods = [round(len(timeseries) / (value * self.perDayLen)) * self.perDayLen for value in freq]
        periods = sorted(list(set(periods) - set([0])),reverse=True)
        for lags in periods:
            if lags % (self.perDayLen * 7) == 0:
                period = int(lags / (self.perDayLen * 7))
                break
            if lags % self.perDayLen == 0:
                period = int(lags / self.perDayLen)
        # self.figshow(timeseries, fftNorm, freq, ffts)
        return period

    def acf_periods(self, timeseries):
        '''
            通过自相关系数求数据周期
        '''
        periods, period = {}, None
        lags = np.array([timedelta(days=1) / timedelta(seconds=self.granularity),
                         timedelta(days=7) / timedelta(seconds=self.granularity)]).astype(int)
        for lag in lags:
            acf_score = acf(timeseries, nlags=lag)[-1]
            periods[lag] = acf_score
            print(f"lag: {lag} fft acf: {acf_score}")
        periods = dict(sorted(periods.items(), key=lambda t: t[1], reverse=True))

        for lags, score in periods.items():
            if score >= 0.5 and lags % (self.perDayLen * 7) == 0:
                period = int(lags / (self.perDayLen * 7))
                break
            if score >= 0.5 and lags % self.perDayLen == 0:
                period = int(lags / self.perDayLen)
        return period

    def get_periods(self, timeseries):

        if self.getPeriodMethod == 'fft':
            period = self.fft_periods(timeseries)
        else:
            period = self.acf_periods(timeseries)
        return period

    def figshow(self, timeseries, yfhalf, xMax, yMax):
        plt.subplot(211)
        x = np.arange(len(timeseries))  # x轴
        xhalf = list(range(int(len(timeseries) / 2)))
        plt.plot(x, timeseries)
        plt.title('Original wave')

        yfhalf[0] = 0
        plt.subplot(212)
        plt.plot(xhalf, yfhalf, 'r')
        plt.title('FFT of Mixed wave(half side frequency range)', fontsize=10, color='#7A378B')  # 注意这里的颜色可以查询颜色代码表

        plt.plot(xMax, yMax, 'o', c='yellow')
        plt.show(block=False)
        plt.show()
