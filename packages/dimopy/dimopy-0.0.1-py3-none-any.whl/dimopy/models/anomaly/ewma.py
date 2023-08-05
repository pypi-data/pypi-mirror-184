# -*- coding: utf-8 -*-
from typing import Union, Any
from numpy import mean, sqrt, var


class EWMAMonitor(object):

    def __init__(self, alpha=0.3, coefficient=3):
        """
        :param alpha: Discount rate of ewma, usually in (0.2, 0.3).
        :param coefficient: Coefficient is the width of the control limits, usually in (2.7, 3.0).
        """
        self.alpha = alpha
        self.coefficient = coefficient

    def predict(self, data):
        """
        Predict if a particular sample is an outlier or not.
        param data: the time data to detect of
        """
        s: list[Union[float, Any]] = [data[0]]

        for i in range(1, len(data)):
            temp = self.alpha * data[i] + (1 - self.alpha) * s[-1]
            s.append(temp)
        s_avg = mean(s)
        sigma = sqrt(var(data))
        upper = s_avg + self.coefficient * sigma * sqrt(self.alpha / (2 - self.alpha))
        lower = s_avg - self.coefficient * sigma * sqrt(self.alpha / (2 - self.alpha))

        return lower, upper
