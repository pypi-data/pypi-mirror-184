from dimopy.error.response import res_error


def catch(func):
    """
    异常捕获
    :param func: 装饰器
    :return: 返回自行接收
    """

    def wrapper(*args, **kw):
        # func.__name__
        try:
            res = func(*args, **kw)
        except Exception as e:
            # 异常封装为抛出的异常
            # return res_error(e)
            exit()
        else:
            return res

    return wrapper


def export(func):
    """
    外部调用必然返回结果
    :param func: 装饰器
    :return: 返回成功或失败
    """

    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except Exception as e:
            # 异常封装为抛出的异常
            return res_error(str(e))

    return wrapper
