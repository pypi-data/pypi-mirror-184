from __future__ import annotations

import dimopy.core.common as com

from pandas import date_range, DataFrame
from datetime import datetime


def time_range(start=None,
               end=None,
               periods=None,
               freq=None,
               detect_time: str | None = None,
               inclusive="right",
               normalize: bool = False) -> DataFrame:
    """
    pandas date_range
    """

    if start is None:
        start = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

    if freq is None and com.any_none(periods, start, end):
        freq = "1min"

    if com.count_not_none(start, end, periods, freq) != 3:
        raise ValueError(
            "需要设置 start_time, end_time, periods, freq 四个参数中的三个"
        )

    time_index = date_range(start=start, end=end, periods=periods, freq=freq, inclusive=inclusive, normalize=normalize)
    df = DataFrame({'time': time_index})

    # 对时间进行截断
    if detect_time is not None:
        detect_time = [item.strip() for item in detect_time.split(',')]
        df.index = time_index
        df = df.between_time(detect_time[0], detect_time[1])
        df.reset_index(inplace=True, drop=True)

    return df


def calculate_interval(df: DataFrame) -> int:
    """
    calculate time interval, return seconds
    """
    time_mode = df['time'].diff().mode()
    interval = time_mode.values[0].astype('timedelta64[s]').astype(float)
    interval = 60 if interval < 60 else interval
    return int(interval)

