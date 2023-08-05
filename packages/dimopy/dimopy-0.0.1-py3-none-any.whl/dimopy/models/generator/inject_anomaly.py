from numpy import random, zeros, mean


class InjectAnomaly(object):
    def __init__(self, data):

        self.data = data
        self.length = len(data)
        self.label = zeros(self.length, dtype=int)
        self.data_origin = data.copy()
        self.data_max = max(self.data)
        self.data_min = min(self.data)
        self.data_mean = mean(self.data)

    def point_contextual_outliers(self, ratio, factor, radius):
        """
        Add point contextual outliers to original data
        Args:
            ratio: what ratio outliers will be added
            factor: the larger, the outliers are farther from inliers
                    Notice: point contextual outliers will not exceed the range of [min, max] of original data
            radius: the radius of collective outliers range
        """
        position = (random.rand(round(self.length * ratio)) * self.length).astype(int)
        for i in position:
            local_std = self.data_origin[max(0, i - radius):min(i + radius, self.length)].std()
            coef = factor * local_std

            if coef >= 1:
                if (self.data_origin[i] * coef - self.data[i]) / self.data_max > 0.2:
                    self.data[i] = self.data_origin[i] + self.data_max * random.normal(0, 0.5)
                    # self.label[i] = 1
            else:
                if (self.data[i] - self.data_origin[i] * coef) / self.data_max > 0.2:
                    self.data[i] = self.data_origin[i] * coef
                    # self.label[i] = 1
            
    def collective_trend_outliers(self, ratio, factor, radius):
        """
        Add collective trend outliers to original data
        Args:
            ratio: what ratio outliers will be added
            factor: how dramatic will the trend be
            radius: the radius of collective outliers range
        """
        position = (random.rand(round(self.length * ratio / (2 * radius))) * self.length).astype(int)
        for i in position:
            start, end = max(0, i - radius), min(self.length, i + radius)
            slope = random.choice([-1, 1]) * factor * mean(self.data_origin[start:end])
            self.data[start:end] = self.data_origin[start:end] + slope
            self.label[start:end] = 1

