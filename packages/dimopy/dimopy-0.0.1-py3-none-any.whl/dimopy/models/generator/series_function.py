import numpy as np


def sine(length, freq=0.04, coef=1.5, offset=0.0, noise_level=0.05):
    timestamp = np.arange(length)
    value = np.sin(2 * np.pi * freq * timestamp)
    if noise_level != 0:
        noise = np.random.normal(0, 1, length)
        value = value + noise_level * noise
    value = coef * value + offset
    if min(value) < 0:
        value = value + abs(min(value))
    return value


def cosine(length, freq=0.04, coef=1.5, offset=0.0, noise_level=0.05):
    timestamp = np.arange(length)
    value = np.cos(2 * np.pi * freq * timestamp)
    if noise_level != 0:
        noise = np.random.normal(0, 1, length)
        value = value + noise_level * noise
    value = coef * value + offset
    if min(value) < 0:
        value = value + abs(min(value))
    return value


def square_sine(level=5, length=1440, freq=0.04, coef=1.5, offset=0.0, noise_level=0.05):
    value = np.zeros(length)
    for i in range(level):
        value += 1 / (2 * i + 1) * sine(length=length, freq=freq * (2 * i + 1), coef=coef, offset=offset,
                                        noise_level=noise_level)
    return value


def series_segmentation(data, step_size=1):
    return np.split(data, np.where(np.diff(data) != step_size)[0] + 1)
