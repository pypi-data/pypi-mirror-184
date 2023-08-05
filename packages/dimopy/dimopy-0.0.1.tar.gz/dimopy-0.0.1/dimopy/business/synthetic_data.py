import dimopy.core.common as com
from pandas import date_range, DataFrame
from datetime import datetime
from dimopy.models.generator.univariate_module import univariate_model
from dimopy.models.generator.multivariate_module import multivariate_model
import pandas as pd
import numpy as np
seed = 2022
np.random.seed(seed)


class SyntheticModel(object):

    def __init__(self, parameters=None):
        self.df = None
        self.parameters = None
        self.__init_parameters(parameters)
        self.__gen_timestamp()

    def __init_parameters(self, parameters):
        """

        @param parameters:
        @return:
        """

        parameters = dict() if parameters is None else parameters
        default_parameters = {"start_time": None,
                              "end_time": None,
                              "length": 1440 * 7,
                              "freq": "1min",
                              "detect_time": None}
        default_parameters.update(parameters)

        self.parameters = default_parameters

    def __gen_timestamp(self):

        start = self.parameters['start_time']
        freq = self.parameters['freq']
        periods = self.parameters['length']
        end = self.parameters['end_time']

        if start is None:
            start = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

        if freq is None and com.any_none(periods, start, end):
            freq = "1min"

        if com.count_not_none(start, end, periods, freq) != 3:
            raise ValueError(
                "需要设置 start_time, end_time, periods, series_freq 四个参数中的三个"
            )

        time_range = date_range(start=start, end=end, periods=periods, freq=freq)
        df = DataFrame({'time': time_range})

        # 对时间进行截断
        if self.parameters['detect_time'] is not None:
            self.parameters['detect_time'] = [item.strip() for item in self.parameters['detect_time'].split(',')]
            df.index = time_range
            df = df.between_time(self.parameters['detect_time'][0], self.parameters['detect_time'][1])
            df.reset_index(inplace=True, drop=True)

        series_length = len(df)
        self.parameters['series_length'] = series_length

        self.df = df
        return self.df

    def univariate(self, period=1440, coef=1.5, offset=0, noise_level=0.05, ratio=0.05, radius=5, factor=1, label=True):
        freq = 1.0 / period
        length = self.parameters['series_length']
        behavior_config = [{'freq': freq, 'coef': coef, "offset": offset, 'noise_level': noise_level}]
        data_object = univariate_model(length=length, ratio=ratio, radius=radius, factor=factor,
                                       behavior_config=behavior_config)
        self.df['value'] = data_object.data
        self.df.loc[self.df['value'] < 0, 'value'] = 0
        if label:
            self.df['label'] = data_object.label
        return self.df

    def multivariate(self, dim=1, label=True):
        data_object = multivariate_model(self.parameters)
        columns = [f'col_{i}' for i in range(dim)]
        df_cat = pd.DataFrame(data_object.data.T)
        df_cat.columns = columns
        self.df = pd.concat([self.df, df_cat], axis=1)

        if label:
            self.df['label'] = data_object.label
        return self.df

