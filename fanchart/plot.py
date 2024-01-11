import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
from twopiece.scale import tpnorm
import pkg_resources

register_matplotlib_converters()

DARK_BG = "#212946"
dark_mpl_rc_context = {
    "lines.color": "white",
    "patch.edgecolor": "white",
    "text.color": 'white',
    "axes.facecolor": DARK_BG,
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "lightgray",
    "figure.facecolor": DARK_BG,
    "figure.edgecolor": DARK_BG,
    "savefig.facecolor": DARK_BG,
    "savefig.edgecolor": DARK_BG}


def load_boe_parameters():
    """
    Loads a table with parameters to test the fan function
    :return: dataframe
    """
    parameters = pkg_resources.resource_stream(__name__, 'data/fan_parameters_2022Q3.csv')
    print("Loading 2022Q3 parameters - as published by the BoE.")
    return pd.read_csv(parameters)


def load_boe_history():
    """
    Loads a table with historical/observed CPI inflation values
    :return: dataframe
    """
    history = pkg_resources.resource_stream(__name__, 'data/fan_history_2022Q3.csv')
    print("Loading 2022Q3 historic CPI inflation data  - as published by the BoE.")
    return pd.read_csv(history)


def _get_alphas(p):
    n = len(p)
    a = [round(-3.951 * x * x + 3.951 * x + 0.012345, 2) for x in p]

    if len(a) % 2 == 0:
        index = int(n / 2)
    else:
        index = int((n - 1) / 2)

    alpha = a[:index] + a[index + 1:]

    return alpha


def _color_setup(darkmode):
    # plt.rcParams.update(plt.rcParamsDefault)
    if darkmode:
        plt.rcParams.update({
            "lines.color": "white",
            "patch.edgecolor": "white",
            "text.color": 'white',
            "axes.facecolor": DARK_BG,
            "axes.edgecolor": "lightgray",
            "axes.labelcolor": "white",
            "xtick.color": "white",
            "ytick.color": "white",
            "grid.color": "lightgray",
            "figure.facecolor": DARK_BG,
            "figure.edgecolor": DARK_BG,
            "savefig.facecolor": DARK_BG,
            "savefig.edgecolor": DARK_BG})


def _fan_single_customised(p, loc, sigma, gamma, kind='pdf', color='xkcd:tomato red', hide_xgrid=True,
                           **fig_kw):
    dist = tpnorm(loc=loc, sigma=sigma, gamma=gamma, kind='boe')
    q = dist.ppf(p)
    x = np.linspace(loc - 4 * sigma, loc + 4 * sigma, 500)

    fig = plt.figure(**fig_kw)
    ax = fig.add_subplot(111)
    ax.spines[['top', 'right', 'left']].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.tick_right()
    ax.yaxis.set_ticks_position('left')
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
        raise ValueError("Invalid kind provided. Kind must be either pdf or cdf")

    ax.set_yticks(y_values)
    ax.set_yticklabels(y_labs)
    ax.set_title(title, loc='right')

    if hide_xgrid:
        ax.grid(axis='y', alpha=0.25)
        ax.grid(axis='x', alpha=0.0)
        ax.set_axisbelow(True)

    alpha_fill = _get_alphas(p)
    for i in np.arange(0, len(q) - 1):
        x = np.linspace(q[i], q[i + 1])
        if kind == 'pdf':
            y = dist.pdf(x)
        elif kind == 'cdf':
            y = dist.cdf(x)
        else:
            raise ValueError("Invalid kind provided. Kind must be either pdf or cdf")
        plt.fill_between(x, y, alpha=alpha_fill[i], facecolor=color, edgecolor="none", linewidth=0.0)

    plt.show()

    return fig


def fan_single(loc, sigma, gamma, probs, kind='pdf', color='xkcd:tomato red', **fig_kw):
    """
    Returns a fan_single chart
    :param loc: Mode parameter (double)
    :param sigma: Uncertainty parameter (double >0)
    :param gamma: Skewness parameter (double)
    :param probs: Probabilities to make the fan chart
    :param kind: Either pdf or cdf
    :param color: A color to make the chart
    :return: fanchart single (figure)
    """
    return _fan_single_customised(probs, loc, sigma, gamma, kind=kind, color=color, **fig_kw)


@mpl.rc_context(dark_mpl_rc_context)
def fan_single_dark(loc, sigma, gamma, probs, kind='pdf', color='orange', **fig_kw):
    """
    Returns a fan_single chart
    :param loc: Mode parameter (double)
    :param sigma: Uncertainty parameter (double >0)
    :param gamma: Skewness parameter (double)
    :param probs: Probabilities to make the fan chart
    :param kind: Either pdf or cdf
    :param color: A color to make the chart
    :return: fanchart single (figure)
    """

    return _fan_single_customised(probs, loc, sigma, gamma, kind=kind, color=color, **fig_kw)


def _fan_customised(data, p, historic=None, color='cornflowerblue', title='CPI Inflation Projection',
                    title_loc='left', darkmode=False, hide_xgrid=True,
                    **fig_kw):
    dat = data.copy()
    dat['Date'] = pd.to_datetime(dat['Date'])
    dat = dat.reset_index()
    max_historical_value = 0
    min_historical_value = 0

    fig = plt.figure(**fig_kw)
    ax = fig.add_subplot(111)
    ax.spines[['top', 'right', 'left']].set_visible(False)

    ax.set_title(title, loc=title_loc)
    ax.xaxis.set_ticks_position('bottom')
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_minor_locator(mdates.MonthLocator((1, 4, 7, 10)))

    results = np.zeros((dat.shape[0], len(p)))
    for idx, _ in enumerate(results):
        mode = dat['Mode'][idx]
        sigma = dat['Uncertainty'][idx]
        gamma = dat['Skewness'][idx]
        dist = tpnorm(loc=mode, sigma=sigma, gamma=gamma, kind='boe')
        results[idx] = dist.ppf(p)
    results = pd.DataFrame(results, columns=p, index=dat['Date'])

    if historic is not None:
        hist = historic.copy()
        hist['Date'] = pd.to_datetime(hist['Date'])
        min_historical_value = min(hist['Inflation'])
        max_historical_value = max(hist['Inflation'])
        anchor_date = hist.iloc[-1]['Date']
        anchor_value = hist.iloc[-1]['Inflation']
        results.loc[anchor_date] = np.repeat(anchor_value, results.shape[1])
        max_date = dat['Date'].loc[dat.shape[0] - 1]
        if darkmode:
            ax.axvspan(anchor_date, max_date, color='white', alpha=0.4, label='Projection')
        else:
            ax.axvspan(anchor_date, max_date, color='gray', alpha=0.2, label='Projection')
        plt.plot(hist['Date'], hist['Inflation'], color=color, marker='', linewidth=2.0)

    results = results.sort_index()
    alpha_fill = _get_alphas(p)

    for idx, column in enumerate(results.columns):
        if idx < results.shape[1] - 1:
            plt.fill_between(results.index, results.iloc[:, idx], results.iloc[:, idx + 1],
                             alpha=alpha_fill[idx], facecolor=color, edgecolor="none", linewidth=0.0)

    if darkmode:
        ax.axhline(y=2.0, color='white', linestyle='--', linewidth=1.5)
    else:
        ax.axhline(y=2.0, color='black', linestyle='--', linewidth=1.5)

    min_inflation = min(min_historical_value, np.min(results.to_numpy()))
    max_inflation = max(max_historical_value, np.max(results.to_numpy()))
    ax.yaxis.tick_left()
    ax.set_yticks([t for t in range(round(min_inflation) - 2, round(max_inflation) + 2) if t % 2 == 0])
    ax.set_ylim([round(min_inflation) - 2., round(max_inflation) + 2.])
    ax.legend(loc='lower left', frameon=False)

    if hide_xgrid:
        ax.grid(axis='y', alpha=0.25)
        ax.grid(axis='x', alpha=0.0)
        ax.set_axisbelow(True)

    ax1 = ax.twinx()
    ax1.set_yticks(ax.get_yticks())
    ax1.set_ylim(ax.get_ylim())
    ax1.spines[['top', 'right', 'left']].set_visible(False)

    plt.show()

    return fig


def fan(pars, probs, historic=None, color='xkcd:tomato red', title='CPI Inflation Projection', **fig_kw):
    """
    Returns a fanchart
    :param pars: dataframe - Parameters table with columns Mode, Uncertainty, Skewness
    :param probs: list- Probabilities to make the fan chart
    :param historic: dataframe - Historical/observed values table with columns Date, Inflation
    :param color: string - color for the chart
    :param title: string - title for the chart
    :return: fanchart (figure)
    """
    return _fan_customised(pars, probs, historic=historic, color=color, darkmode=False, title=title, **fig_kw)


@mpl.rc_context(dark_mpl_rc_context)
def fan_dark(pars, probs, historic=None, color='orange', title='CPI Inflation Projection', **fig_kw):
    """
    Returns a fanchart in dark mode
    :param pars: dataframe - Parameters table with columns Mode, Uncertainty, Skewness
    :param probs: list- Probabilities to make the fan chart
    :param historic: dataframe - Historical/observed values table with columns Date, Inflation
    :param color: string - color for the chart
    :param title: string - title for the chart
    :return: fanchart (figure)
    """
    return _fan_customised(pars, probs, historic=historic, color=color, darkmode=True, title=title, **fig_kw)
