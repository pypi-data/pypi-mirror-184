import numpy as np
import pandas as pd
from numpy import mean, median, repeat, ceil
from typing import Optional
from prophet import Prophet


class UnivariateProphet(object):
    def __init__(self,
                 per_day_length: int = 1440,
                 periods: int = 7,
                 mode: str = 'mean',
                 pred_length: int = 1
                 ):

        self.reshape_size = None
        self.model = None
        self.per_day_length = per_day_length
        self.periods = periods
        self.pred_length = pred_length
        self.mode = mode

    def fit(self, fit_data: Optional[pd.DataFrame] = None, col_name: str = 'value'):

        if self.mode == 'prophet':
            fit_data.rename(columns={'time': 'ds', col_name: 'y'}, inplace=True)
            self.model = Prophet()
            self.model.fit(fit_data)
        else:
            in_data = fit_data[col_name]
            # 将所有的数据加入训练
            self.reshape_size = int(len(in_data) / (self.per_day_length * self.periods))
            train_data_len = self.reshape_size * self.per_day_length * self.periods

            self.model = in_data[-train_data_len:].values

    def predict(self) -> np.ndarray:
        pred_len = self.pred_length

        if self.mode == 'prophet':
            future = self.model.make_future_dataframe(periods=pred_len)
            forecast = self.model.predict(future)
            predict_array = forecast['yhat'].values
        else:
            reshape_normal = self.model.reshape(self.reshape_size, self.per_day_length * self.periods)
            if self.mode == 'mean':
                predict_array = mean(reshape_normal, axis=0)
            else:
                predict_array = median(reshape_normal, axis=0)

        current_pred_len = len(predict_array)

        if current_pred_len < pred_len:
            repeat_num = ceil(pred_len / current_pred_len)
            predict_list = predict_array.reshape(-1, 1)
            repeat_predict = repeat(predict_list, repeat_num, axis=1).transpose()
            predict_array = repeat_predict.flatten()
        else:
            pass
        predict_array = predict_array[0:pred_len]

        return predict_array
