import os
import json
import pickle
from pandas import DataFrame


def json_to_dataframe(json_array):
    """
    json转dataframe
    :param json_array: json数据
    :return: dataframe
    """

    df = DataFrame.from_dict(json_array, orient='columns')

    if df.empty:
        raise Exception("训练数据为空")

    for col in df.columns.tolist():
        if col == 'time':
            continue
        df[col] = df[col].astype(float)

    return df


def load_json_file(path):
    if os.path.exists(path):
        with open(path, "r") as reader:
            jf = json.load(reader)
        return jf
    raise Exception("{} 路径不存在。".format(path))


def load_pkl_file(path):
    if os.path.exists(path):
        with open(path, "rb") as reader:
            model = pickle.load(reader)
        return model
    raise Exception("{} 路径不存在。".format(path))


def save_pkl_file(model, path):
    if not os.path.exists(path):
        with open(path, "wb") as writer:
            pickle.dump(model, writer)
    else:
        raise Exception("{} 文件已存在！".format(path))
