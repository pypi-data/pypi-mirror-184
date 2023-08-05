import numpy as np

from dimopy.models.generator.series_function import series_segmentation, sine, cosine, square_sine
from dimopy.models.generator.anomaly_type import collective_global_synthetic


class UnivariateDataGenerator(object):
    def __init__(self, stream_length, behavior=sine, behavior_config=None):

        self.stream_length = stream_length
        self.behavior = behavior
        self.behavior_config = behavior_config if behavior_config is not None else {}

        self.data = None
        self.label = None
        self.data_origin = None
        self.timestamp = np.arange(self.stream_length)

        self.generate_timeseries()

    def generate_timeseries(self):
        self.behavior_config['length'] = self.stream_length
        self.data = self.behavior(**self.behavior_config)
        self.data_origin = self.data.copy()
        self.label = np.zeros(self.stream_length, dtype=int)

    def point_contextual_outliers(self, ratio, factor, radius):
        """
        Add point contextual outliers to original data
        Args:
            ratio: what ratio outliers will be added
            factor: the larger, the outliers are farther from inliers
                    Notice: point contextual outliers will not exceed the range of [min, max] of original data
            radius: the radius of collective outliers range
        """
        position = (np.random.rand(round(self.stream_length * ratio)) * self.stream_length).astype(int)
        maximum, minimum = max(self.data), min(self.data)
        for i in position:
            local_std = self.data_origin[max(0, i - radius):min(i + radius, self.stream_length)].std()
            self.data[i] = self.data_origin[i] * factor * local_std
            if self.data[i] > maximum:
                self.data[i] = maximum * min(0.95, abs(np.random.normal(0, 0.5)))  # previous(0, 1)
            if self.data[i] < minimum:
                self.data[i] = minimum * min(0.95, abs(np.random.normal(0, 0.5)))

            self.label[i] = 1

    def collective_global_outliers(self, ratio, radius, option='square', coef=3., noise_level=0.0,
                                   level=5, freq=0.04, offset=0.0,  # only used when option=='square'
                                   base=None):  # only used when option=='other'
        """
        Add collective global outliers to original data
        Args:
            ratio: what ratio outliers will be added
            radius: the radius of collective outliers range
            option: if 'square': 'level' 'freq' and 'offset' are used to generate square sine wave
                    if 'other': 'base' is used to generate outlier shape
            level: how many sine waves will square_wave synthesis
            base: a list of values that we want to substitute inliers when we generate outliers
            :param noise_level:
            :param coef:
            :param option:
            :param radius:
            :param ratio:
            :param base:
            :param level:
            :param freq:
            :param offset:
        """
        if base is None:
            base = [0., ]
        position = (np.random.rand(round(self.stream_length * ratio / (2 * radius))) * self.stream_length).astype(int)

        valid_option = {'square', 'other'}
        if option not in valid_option:
            raise ValueError("'option' must be one of %r." % valid_option)

        if option == 'square':
            sub_data = square_sine(level=level, length=self.stream_length, freq=freq,
                                   coef=coef, offset=offset, noise_level=noise_level)
        else:
            sub_data = collective_global_synthetic(length=self.stream_length, base=base,
                                                   coef=coef, noise_level=noise_level)
        for i in position:
            start, end = max(0, i - radius), min(self.stream_length, i + radius)
            self.data[start:end] = sub_data[start:end]
            self.label[start:end] = 1

    def collective_trend_outliers(self, ratio, factor, radius):
        """
        Add collective trend outliers to original data
        Args:
            ratio: what ratio outliers will be added
            factor: how dramatic will the trend be
            radius: the radius of collective outliers range
        """
        position = (np.random.rand(round(self.stream_length * ratio / (2 * radius))) * self.stream_length).astype(int)
        for i in position:
            start, end = max(0, i - radius), min(self.stream_length, i + radius)
            slope = np.random.choice([-1, 1]) * factor * np.arange(end - start)
            self.data[start:end] = self.data_origin[start:end] + slope
            self.data[end:] = self.data[end:] + slope[-1]/5
            self.label[start:end] = 1

    def collective_seasonal_outliers(self, ratio, factor, radius):
        """
        Add collective seasonal outliers to original data
        Args:
            ratio: what ratio outliers will be added
            factor: how many times will frequency multiple
            radius: the radius of collective outliers range
        """
        position = (np.random.rand(round(self.stream_length * ratio / (2 * radius))) * self.stream_length).astype(int)
        seasonal_config = self.behavior_config
        seasonal_config['freq'] = factor * self.behavior_config['freq']
        for i in position:
            start, end = max(0, i - radius), min(self.stream_length, i + radius)
            self.data[start:end] = self.behavior(**seasonal_config)[start:end]
            self.label[start:end] = 1


def univariate_model(length=1440, ratio=0.001, factor=1, radius=10, behavior_config=None):
    behavior_config = behavior_config[0]
    freq = behavior_config['freq']
    coef = behavior_config['coef']
    noise_level = behavior_config['noise_level']
    offset = behavior_config['offset']

    base = [1.4529900e-01, 1.2820500e-01, 9.4017000e-02, 7.6923000e-02, 1.1111100e-01, 1.4529900e-01, 1.7948700e-01,
            2.1367500e-01, 2.1367500e-01]
    univariate_data = UnivariateDataGenerator(stream_length=length, behavior=sine, behavior_config=behavior_config)

    univariate_data.collective_global_outliers(ratio=ratio, radius=radius, option='square', coef=coef,
                                               noise_level=noise_level,
                                               level=3, freq=freq,
                                               base=base, offset=offset)  # 2
    univariate_data.collective_seasonal_outliers(ratio=ratio, factor=factor, radius=radius)  # 3
    univariate_data.collective_trend_outliers(ratio=ratio, factor=factor, radius=radius)  # 4
    univariate_data.point_contextual_outliers(ratio=ratio, factor=factor, radius=radius)  # 1

    return univariate_data
