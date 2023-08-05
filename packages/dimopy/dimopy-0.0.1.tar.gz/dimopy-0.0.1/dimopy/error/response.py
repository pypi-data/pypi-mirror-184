# 成功返回
def success(data: dict):
    res = dict()
    res["code"] = 200
    res["msg"] = "success"
    res["data"] = data
    return res


# 异常返回
def res_error(msg, data=None):
    if data is None:
        data = {}
    res = dict()
    res["code"] = 500
    res["msg"] = str(msg)
    res["data"] = data
    return res
