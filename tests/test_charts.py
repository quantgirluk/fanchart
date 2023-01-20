from fanchart import load_boe_parameters, load_boe_history, fan, fan_single, fan_dark, fan_single_dark
import numpy as np


def test_plot_fan():
    parameters = load_boe_parameters()
    history = load_boe_history()
    probs = np.arange(0.05, 1, 0.05)
    fan(pars=parameters, probs=probs, historic=history)
    fan(pars=parameters, probs=probs, historic=history[history.Date >= '2018'])
    fan(pars=parameters, probs=np.arange(0.05, 1, 0.05), historic=history[history.Date >= '2018'], color='teal')
    fan_dark(pars=parameters, probs=np.arange(0.05, 1, 0.05), historic=history[history.Date >= '2018'], color='cyan')

def test_fan_single():
    parameters = load_boe_parameters()
    pars = parameters.iloc[4]
    loc = pars.Mode
    sigma = pars.Uncertainty
    gamma = pars.Skewness
    probs = [0.05, 0.20, 0.35, 0.65, 0.80, 0.95]
    fan_single(loc=loc, sigma=sigma, gamma=gamma, probs=probs, kind='pdf')
    fan_single(loc=loc, sigma=sigma, gamma=gamma, probs=probs, kind='cdf')
    fan_single_dark(loc=loc, sigma=sigma, gamma=gamma, probs=probs, kind='cdf')
