# -*- coding: utf-8 -*-
from numpy import std, mean


class KSigmaMonitor(object):

    def __init__(self, k: float = 3.0):
        self.k = k

    def predict(self, data):
        _mean, _std = mean(data), std(data)
        lower, upper = _mean - self.k * _std, _mean + self.k * _std
        return lower, upper
