import plotly.graph_objs as go
import plotly as py
import matplotlib.pyplot as plt

from datetime import timedelta
from plotly.subplots import make_subplots
from pandas import to_datetime, merge, DataFrame
from dimopy.utils.datetimes import calculate_interval, time_range

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def plot_anomaly_png(data, col='value', path=None):
    pass


def plot_anomaly_html(data, col='value', path=None, auto_open=True):
    fig = make_subplots()
    fig = go.FigureWidget(fig)
    data.index = data['time']

    label = data[data['label'] == 1]
    fig.add_trace(go.Scatter(x=data.index.values, y=data[col], mode='lines+text', name='value'))
    fig.add_trace(go.Scatter(x=label.index.values, y=label[col], mode='markers+text',
                             line=dict(color='red', width=2.5), name='label'))

    fig.update_layout(xaxis_rangeslider_visible=True, xaxis_rangeslider_thickness=0.04)
    fig["layout"]["template"] = "seaborn"

    if path is not None:
        py.offline.plot(fig, filename=f'{path}', auto_open=auto_open)
    else:
        fig.show()


def plot_baseline_png(data, col='value', path=None):
    pass


def plot_baseline_html(data, col='value', path=None):
    fig = make_subplots()
    fig = go.FigureWidget(fig)
    data.index = data['time']
    col_list = data.columns.tolist()

    label = data[data['label'] == 1]
    fig.add_trace(go.Scatter(x=data.index.values, y=data[col], mode='lines+text', name='value'))

    if 'predict' in col_list:
        fig.add_trace(go.Scatter(x=data.index.values, y=data['predict'].values, mode='lines+text', name='predict'))
    fig.add_trace(go.Scatter(x=data.index.values, y=label[col], mode='markers+text',
                             line=dict(color='red', width=2.5), name='label'))
    fig.add_trace(go.Scatter(x=data.index.values, y=data['upper'], name='upper', line=dict(width=0.1)), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index.values, y=data['lower'], name='lower', line=dict(width=0.1), fill='tonextx',
                             fillcolor='rgba(0,191,255,0.4)'), row=1, col=1)

    fig.update_layout(xaxis_rangeslider_visible=True, xaxis_rangeslider_thickness=0.04)
    fig["layout"]["template"] = "seaborn"

    if path is not None:
        py.offline.plot(fig, filename=f'{path}', auto_open=True)
    else:
        fig.show()


def plot_history_html(data: DataFrame = None,
                      col: str = 'value',
                      period: int = 1,
                      path: str = None,
                      auto_open: bool = True):

    len_data = len(data)
    data.drop_duplicates(inplace=True)
    len_data_dp = len(data)

    if len_data - len_data_dp > 0:
        print(f'数据存在重复，重复条数{len_data - len_data_dp}')

    data.drop_duplicates(subset=['time'], inplace=True, keep='first')

    len_data_dpt = len(data)
    if len_data_dp - len_data_dpt > 0:
        print(f'去重后时间点存在重复，重复条数{len_data_dp - len_data_dpt}')

    data['time'] = to_datetime(data['time'])
    data.sort_values(by='time', ascending=True, inplace=True)

    # 时间颗粒度
    interval = calculate_interval(data)

    # 每天的点数
    per_day_len = int(86400 / interval)

    # 时间戳重采样
    freq = f'{int(interval / 60)}min'
    data.set_index('time', inplace=True)
    data = data.resample(freq).mean()
    data.reset_index(inplace=True)

    start_time, end_time = data['time'].iloc[0], data['time'].iloc[-1] + timedelta(days=1)
    df_normalize = time_range(start=start_time, end=end_time, freq=freq, normalize=True, inclusive='both')

    df_merge = merge(data, df_normalize.iloc[:-1, :], how='right', on='time')
    value_array = df_merge['value'].values
    len_merge = len(df_merge)

    if period == 0:
        plot_html(df_merge, col=col, path=path, auto_open=auto_open)
    else:
        value_plot = value_array.reshape(per_day_len*period, int(len_merge/(per_day_len*period)))
        df_plot = DataFrame(value_plot)
        df_plot.columns = [f'col_{i}' for i in range(df_plot.shape[1])]
        data_list = []
        for iter_col in df_plot.columns:
            data_list.append(go.Scatter(x=df_plot.index, y=df_plot[iter_col], name=iter_col))
        fig = go.Figure(data=data_list)
        fig.show()


def plot_html(data, col='value', path=None, auto_open=True):
    fig = make_subplots()
    fig = go.FigureWidget(fig)

    fig.add_trace(go.Scatter(x=data.index.values, y=data[col], mode='lines+text', name=col))

    fig.update_layout(xaxis_rangeslider_visible=True, xaxis_rangeslider_thickness=0.04)
    fig["layout"]["template"] = "seaborn"

    if path is not None:
        py.offline.plot(fig, filename=f'{path}', auto_open=auto_open)
    else:
        fig.show()
