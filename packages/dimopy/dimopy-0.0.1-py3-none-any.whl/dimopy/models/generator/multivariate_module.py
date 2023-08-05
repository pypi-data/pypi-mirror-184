import numpy as np

from dimopy.models.generator.series_function import series_segmentation, sine, cosine, square_sine
from dimopy.models.generator.anomaly_type import collective_global_synthetic


class MultivariateDataGenerator(object):
    def __init__(self, dim, stream_length, behavior, behavior_config=None):

        self.dim = dim
        self.stream_length = stream_length
        self.behavior = behavior if behavior is not None else [sine] * dim
        self.behavior_config = behavior_config if behavior_config is not None else [{}] * dim

        self.data = np.empty(shape=[0, stream_length], dtype=float)
        self.label = None
        self.data_origin = None
        self.timestamp = np.arange(self.stream_length)

        self.generate_timeseries()

    def generate_timeseries(self):
        for i in range(self.dim):
            self.behavior_config[i]['length'] = self.stream_length
            self.data = np.append(self.data, [self.behavior[i](**self.behavior_config[i])], axis=0)
        self.data_origin = self.data.copy()
        self.label = np.zeros(self.stream_length, dtype=int)

    def point_global_outliers(self, dim_no, ratio, factor, radius):
        """
        Add point global outliers to original data
        Args:
            ratio: what ratio outliers will be added
            factor: the larger, the outliers are farther from inliers
            radius: the radius of collective outliers range
            :param radius:
            :param factor:
            :param ratio:
            :param dim_no:
        """
        position = (np.random.rand(round(self.stream_length * ratio)) * self.stream_length).astype(int)
        maximum, minimum = max(self.data[dim_no]), min(self.data[dim_no])
        for i in position:
            local_std = self.data_origin[dim_no][max(0, i - radius):min(i + radius, self.stream_length)].std()
            self.data[dim_no][i] = self.data_origin[dim_no][i] * factor * local_std
            if 0 <= self.data[dim_no][i] < maximum:
                self.data[dim_no][i] = maximum
            if 0 > self.data[dim_no][i] > minimum:
                self.data[dim_no][i] = minimum
            self.label[i] = 1

    def point_contextual_outliers(self, dim_no, ratio, factor, radius):
        """
        Add point contextual outliers to original data
        Args:
            ratio: what ratio outliers will be added
            factor: the larger, the outliers are farther from inliers
                    Notice: point contextual outliers will not exceed the range of [min, max] of original data
            radius: the radius of collective outliers range
            :param radius:
            :param factor:
            :param ratio:
            :param dim_no:
        """
        position = (np.random.rand(round(self.stream_length * ratio)) * self.stream_length).astype(int)
        maximum, minimum = max(self.data[dim_no]), min(self.data[dim_no])
        for i in position:
            local_std = self.data_origin[dim_no][max(0, i - radius):min(i + radius, self.stream_length)].std()
            self.data[dim_no][i] = self.data_origin[dim_no][i] * factor * local_std
            if self.data[dim_no][i] > maximum:
                self.data[dim_no][i] = maximum * min(0.95, abs(np.random.normal(0, 1)))
            if self.data[dim_no][i] < minimum:
                self.data[dim_no][i] = minimum * min(0.95, abs(np.random.normal(0, 1)))

            self.label[i] = 1

    def collective_global_outliers(self, dim_no, ratio, radius, option='square', coef=3.0, noise_level=0.0,
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
            :param base:
            :param offset:
            :param level:
            :param noise_level:
            :param coef:
            :param option:
            :param radius:
            :param ratio:
            :param dim_no:
            :param freq:
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
            self.data[dim_no][start:end] = sub_data[start:end]
            self.label[start:end] = 1

    def collective_trend_outliers(self, dim_no, ratio, factor, radius):
        """
        Add collective trend outliers to original data
        Args:
            ratio: what ratio outliers will be added
            factor: how dramatic will the trend be
            radius: the radius of collective outliers range
            :param radius:
            :param factor:
            :param ratio:
            :param dim_no:
        """
        position = (np.random.rand(round(self.stream_length * ratio / (2 * radius))) * self.stream_length).astype(int)
        for i in position:
            start, end = max(0, i - radius), min(self.stream_length, i + radius)
            slope = np.random.choice([-1, 1]) * factor * np.arange(end - start)
            self.data[dim_no][start:end] = self.data_origin[dim_no][start:end] + slope
            self.data[dim_no][end:] = self.data[dim_no][end:] + slope[-1]
            self.label[start:end] = 1

    def collective_seasonal_outliers(self, dim_no, ratio, factor, radius):
        """
        Add collective seasonal outliers to original data
        Args:
            ratio: what ratio outliers will be added
            factor: how many times will frequency multiple
            radius: the radius of collective outliers range
            :param radius:
            :param factor:
            :param ratio:
            :param dim_no:
        """
        position = (np.random.rand(round(self.stream_length * ratio / (2 * radius))) * self.stream_length).astype(int)
        seasonal_config = self.behavior_config[dim_no]
        seasonal_config['freq'] = factor * self.behavior_config[dim_no]['freq']
        for i in position:
            start, end = max(0, i - radius), min(self.stream_length, i + radius)
            self.data[dim_no][start:end] = self.behavior[dim_no](**seasonal_config)[start:end]
            self.label[start:end] = 1


def multivariate_model(config):
    stream_length = config['series_length']
    dim = config['dim']
    behavior_config = config['series_config']

    if len(behavior_config) < dim:
        behavior_config = behavior_config * dim
        behavior_config = behavior_config[:dim]

    multivariate_data = MultivariateDataGenerator(dim=dim, stream_length=stream_length, behavior=None,
                                                  behavior_config=behavior_config)

    for idx in range(dim):
        noise_level = behavior_config[idx]['noise_level']
        freq = behavior_config[idx]['freq']
        offset = behavior_config[idx]['offset']
        coef = behavior_config[idx]['coef']
        multivariate_data.point_global_outliers(dim_no=idx, ratio=0.05, factor=3.5, radius=5)
        multivariate_data.point_contextual_outliers(dim_no=idx, ratio=0.05, factor=2.5, radius=5)
        multivariate_data.collective_global_outliers(dim_no=idx, ratio=0.05, radius=5, option='square', coef=coef,
                                                     noise_level=noise_level, level=20, freq=freq, offset=offset)
        multivariate_data.collective_seasonal_outliers(dim_no=idx, ratio=0.05, factor=3, radius=5)
        multivariate_data.collective_trend_outliers(dim_no=idx, ratio=0.05, factor=0.5, radius=5)

    return multivariate_data
