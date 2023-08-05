# -*- coding: utf-8 -*-
from numpy import quantile


class BoxMonitor(object):

    def __init__(self, iqr_lower=0.15, iqr_upper=0.85, windows=10, coefficient=1.5):
        self.iqr_lower = iqr_lower
        self.iqr_upper = iqr_upper
        self.windows = windows
        self.coefficient = coefficient

    def predict(self, data):
        """
        Predict if a particular sample is an outlier or not.
        param data: the time data to detect of
        """
        q1, q3 = quantile(data[-self.windows:], self.iqr_lower), quantile(data[-self.windows:], self.iqr_upper)
        iqr = q3 - q1
        lower_q1, upper_q3 = q1 - self.coefficient * iqr, q3 + self.coefficient * iqr

        return lower_q1, upper_q3
