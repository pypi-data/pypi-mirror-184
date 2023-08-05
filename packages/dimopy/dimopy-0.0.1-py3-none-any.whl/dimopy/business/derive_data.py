import numpy as np
import pandas as pd
from typing import Optional
from dimopy.error.catch import export
from dimopy.utils.datetimes import time_range
from dimopy.common.data_preprocessing.data_load import json_to_dataframe
from dimopy.utils.datetimes import calculate_interval
from dimopy.models.generator.inject_anomaly import InjectAnomaly
from sklearn.preprocessing import MinMaxScaler
from dimopy.models.forecasting.univariate_prophet import UnivariateProphet
from dimopy.common.utils import calculate_day_points
seed = 2022
np.random.seed(seed)


class DeriveModel(object):

    def __init__(self,
                 start_time: Optional[str] = None,
                 end_time: Optional[str] = None,
                 mode: str = 'median',
                 length: int = 1440,
                 freq: Optional[str] = None,
                 detect_time: Optional[str] = None,
                 noise_level: float = 0.01,
                 periods: int = 1,
                 weight: float = 0.5
                 ):

        self.start_time = start_time
        self.end_time = end_time
        self.mode = mode
        self.periods = periods
        self.length = length
        self.freq = freq
        self.detect_time = detect_time
        self.noise_level = noise_level
        self.weight = weight

    # @export
    def derive(self,
               json_data,
               label: bool = True) -> pd.DataFrame:
        data = json_to_dataframe(json_data)

        if data.empty:
            raise Exception("输入数据为空")

        data = data.sort_values(by=['time'], ascending=True)
        data.drop_duplicates(subset='time', keep='last', inplace=True)
        data['time'] = pd.to_datetime(data['time'])
        len_data = len(data)

        # 获取最后的时间，即新数据开始的时间
        if self.start_time is None:
            self.start_time = data['time'].iloc[-1]

        if self.freq is None:
            granularity = calculate_interval(data)
            self.freq = f'{int(granularity / 60)}min'
        else:
            granularity = 60
        per_day_length = calculate_day_points(granularity)

        # 数据衍生
        df_derive = time_range(start=self.start_time, end=self.end_time, freq=self.freq,
                               periods=self.length + 1, detect_time=self.detect_time)
        len_derive = len(df_derive)
        repeat_num = int(len_derive / len_data) + 1
        data_array = data['value'].values

        array_reshape = data_array.reshape(-1, 1)
        array_repeat = array_reshape.repeat(repeat_num, axis=1).transpose()

        # 原始值
        array_derive = array_repeat.flatten()[0:len_derive]

        # prophet
        derive_obj = UnivariateProphet(mode=self.mode, per_day_length=per_day_length,
                                       pred_length=self.length, periods=self.periods)

        derive_obj.fit(data)
        array_derive_prophet = derive_obj.predict()

        array_derive = array_derive_prophet * (1 - self.weight) + array_derive * self.weight

        # 插入噪声
        scaler = MinMaxScaler()
        data_scaler = scaler.fit_transform(array_derive.reshape(-1, 1))

        if self.noise_level != 0:
            noise = np.random.normal(0, 1, len_derive)
            data_scaler = data_scaler.flatten() + self.noise_level * noise
        else:
            data_scaler = data_scaler.flatten()

        data_inverse = scaler.inverse_transform(data_scaler.reshape(-1, 1))

        # 注入异常 --对率值的指标特殊处理（响应率、成功率）
        obj = InjectAnomaly(data_inverse)
        # obj.collective_trend_outliers(ratio=0.01, factor=3, radius=100)
        obj.point_contextual_outliers(ratio=0.01, factor=1.5, radius=10)

        df_derive['value'] = obj.data
        df_derive.loc[df_derive['value'] < 0, 'value'] = 0

        if label:
            df_derive['label'] = obj.label

        return df_derive
