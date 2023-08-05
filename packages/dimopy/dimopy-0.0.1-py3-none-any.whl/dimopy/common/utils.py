
def calculate_day_points(granularity: int = 60):
    """
        根据颗粒度计算每天的点数，每天的点数至少为1
    """
    per_day_len = int(86400 / granularity)
    return per_day_len
