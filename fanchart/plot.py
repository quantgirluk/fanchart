import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
from twopiece.scale import tpnorm
import pkg_resources

register_matplotlib_converters()


def load_boe_parameters():
    parameters = pkg_resources.resource_stream(__name__, 'data/fan_parameters.csv')
    return pd.read_csv(parameters)


def load_boe_history():
    history = pkg_resources.resource_stream(__name__, 'data/fan_history.csv')

    return pd.read_csv(history)


def get_alphas(p):
    n = len(p)
    a = [round(-3.951 * x * x + 3.951 * x + 0.012345, 2) for x in p]

    if len(a) % 2 == 0:
        index = int(n / 2)
    else:
        index = int((n - 1) / 2)

    alpha = a[:index] + a[index + 1:]

    return alpha


def fan_single(p, loc, sigma, gamma, kind='pdf', color='xkcd:tomato red', grid=False, figsize=None):
    dist = tpnorm(loc=loc, sigma=sigma, gamma=gamma, kind='boe')
    q = dist.ppf(p)
    x = np.linspace(loc - 4 * sigma, loc + 4 * sigma, 500)

    if figsize:
        fig_size =figsize
    else:
        fig_size=(9,6)

    fig = plt.figure(figsize=fig_size)
    ax = fig.add_subplot(111)
    ax.grid(grid)

    ax.xaxis.set_ticks_position('bottom')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.tick_right()
    ax.yaxis.set_ticks_position('both')
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))

    if kind == 'pdf':
        y = dist.pdf(x)
        ax.plot(x, y, color=color)
        title = 'Probability Density'
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
        y_values = ax.get_yticks()
        y_labs = ['{:,.2f}'.format(y) for y in y_values]

    elif kind == 'cdf':
        y = dist.cdf(x)
        ax.plot(x, y, color=color)
        title = 'Cumulative Probability - Percent'
        y_values = ax.get_yticks()
        y_labs = ['{:,.0f}'.format(y * 100) for y in y_values]

    else:
        raise ValueError("kind must be either pdf or cdf")

    ax.set_yticks(y_values)
    ax.set_yticklabels(y_labs)
    ax.set_title(title, loc='right')

    alpha_fill = get_alphas(p)

    for i in np.arange(0, len(q) - 1):

        x = np.linspace(q[i], q[i + 1])
        if kind == 'pdf':
            y = dist.pdf(x)
        elif kind == 'cdf':
            y = dist.cdf(x)
        else:
            raise ValueError("kind must be either pdf or cdf")

        plt.fill_between(x, y, alpha=alpha_fill[i], facecolor=color, edgecolor="none", linewidth=0.0)

    plt.show()
    assert isinstance(fig, object)
    return fig


def fan(data, p, historic=None, color='xkcd:tomato red', grid=False, figsize=None):
    marker = ''
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.reset_index()

    max_historical_value = 0
    min_historical_value = 0

    if figsize:
        fig_size = figsize
    else:
        fig_size = (8, 6)

    fig = plt.figure(figsize=fig_size)
    ax = fig.add_subplot(111)
    ax.set_title('Percentage increase in prices on a year earlier', loc='right')
    ax.xaxis.set_ticks_position('bottom')
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_minor_locator(mdates.MonthLocator((1, 4, 7, 10)))
    ax.yaxis.tick_right()
    ax.yaxis.set_ticks_position('both')
    ax.grid(grid)

    results = np.zeros((data.shape[0], len(p)))
    for index, _ in enumerate(results):
        mode = data['Mode'][index]
        sigma = data['Uncertainty'][index]
        gamma = data['Skewness'][index]
        dist = tpnorm(loc=mode, sigma=sigma, gamma=gamma, kind='boe')
        results[index] = dist.ppf(p)
    results = pd.DataFrame(results, columns=p, index=data['Date'])

    if historic is not None:
        hist = historic.copy()
        hist['Date'] = pd.to_datetime(hist['Date'])

        min_historical_value = min(hist['Inflation'])
        max_historical_value = max(hist['Inflation'])

        anchor_date = hist.iloc[-1]['Date']
        anchor_value = hist.iloc[-1]['Inflation']

        results.loc[anchor_date] = np.repeat(anchor_value, results.shape[1])
        max_date = data['Date'].loc[data.shape[0] - 1]
        plt.axvspan(anchor_date, max_date, color='gray', alpha=0.05)
        plt.plot(hist['Date'], hist['Inflation'], color=color, marker=marker, linewidth=2.0)

    results = results.sort_index()
    alpha_fill = get_alphas(p)

    for index, column in enumerate(results.columns):

        if index < results.shape[1] - 1:
            plt.fill_between(results.index, results.iloc[:, index], results.iloc[:, index + 1],
                             alpha=alpha_fill[index], facecolor=color, edgecolor="none", linewidth=0.0)

    ax.axhline(y=2, color='black', linestyle='-', linewidth=0.75)

    min_inflation = min(min_historical_value, results.to_numpy().min())
    max_inflation = max(max_historical_value, results.to_numpy().max())
    ax.set_ylim([min_inflation - 1., max_inflation + 1.])
    plt.show()

    assert isinstance(fig, object)
    return fig
