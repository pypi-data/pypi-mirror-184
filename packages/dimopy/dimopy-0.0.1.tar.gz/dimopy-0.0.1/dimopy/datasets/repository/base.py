# !/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
内置时序数据集相关操作
"""

from typing import Any, Callable, List, Optional, Sequence, Tuple, Union, Dict
import os

import pandas as pd

from paddlets.logger import raise_if_not
from paddlets import TSDataset, TimeSeries
from dimopy.datasets.repository.datasets_config import ETTh1Dataset
from dimopy.datasets.repository.datasets_config import ETTm1Dataset
from dimopy.datasets.repository.datasets_config import ECLDataset
from dimopy.datasets.repository.datasets_config import WTHDataset
from dimopy.datasets.repository.datasets_config import UNIWTHDataset
from dimopy.datasets.repository.datasets_config import NABTEMPDataset
from dimopy.datasets.repository.datasets_config import PSMTRAINDataset
from dimopy.datasets.repository.datasets_config import PSMTESTDataset

DATASETS = {
    UNIWTHDataset.name: UNIWTHDataset,
    ETTh1Dataset.name: ETTh1Dataset,
    ETTm1Dataset.name: ETTm1Dataset,
    ECLDataset.name: ECLDataset,
    WTHDataset.name: WTHDataset,
    NABTEMPDataset.name: NABTEMPDataset,
    PSMTRAINDataset.name: PSMTRAINDataset,
    PSMTESTDataset.name: PSMTESTDataset
}


def dataset_list() -> List[str]:
    """
    获取paddlets内置时序数据集名称列表

    Returns:
        List(str): 数据集名称列表
    """
    return list(DATASETS.keys())


def get_dataset(name: str) -> "TSDataset":
    """
    基于名称获取内置数据集
    
    Args:
        name(str): 数据集名称，可以从dataset_list获取的列表中选取

    Returns:
        TSDataset: 基于内置数据集构建好的TSDataset对象
        
    """
    raise_if_not(
        name in DATASETS,
        f"Invaild dataset name: {name}"
    )
    dataset = DATASETS[name]
    if dataset.type == 'local':
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dataset.path)
    else:
        path = dataset.path
    df = pd.read_csv(path)
    return TSDataset.load_from_dataframe(df, **dataset.load_param)
