from fanchart import load_boe_parameters, load_boe_history, fan, fan_single, fan_dark, fan_single_dark
import numpy as np
import unittest

SAVE = False
SAVE_PATH = '../docs/source/_static/'


class TestFan(unittest.TestCase):
    parameters = load_boe_parameters()
    history = load_boe_history()

    def test_plot_fan(self):
        probs = np.arange(0.05, 1, 0.05)
        pars = self.parameters
        hist = self.history
        fan(pars=pars, probs=probs, historic=hist, figsize=(12, 6))
        fan(pars=pars, probs=probs, historic=hist[hist.Date >= '2018'], title="My First Fan Chart")
        fan_dark(pars=pars, probs=np.arange(0.05, 1, 0.05), historic=hist[hist.Date >= '2018'], )
        # color='cyan')
        fan(pars=pars, probs=np.arange(0.05, 1, 0.05), historic=hist[hist.Date >= '2018'], color='teal')

    def test_fan_single(self):
        parameters = self.parameters
        pars = parameters.iloc[4]
        loc = pars.Mode
        sigma = pars.Uncertainty
        gamma = pars.Skewness
        probs = [0.05, 0.20, 0.35, 0.65, 0.80, 0.95]
        fan_single(loc=loc, sigma=sigma, gamma=gamma, probs=probs, kind='pdf')
        fan_single(loc=loc, sigma=sigma, gamma=gamma, probs=probs, kind='cdf')
        fan_single_dark(loc=loc, sigma=sigma, gamma=gamma, probs=probs, kind='cdf')

    def test_quick_start(self, save=SAVE):
        parameters = self.parameters
        history = self.history
        probs = [0.05, 0.20, 0.35, 0.65, 0.80, 0.95]
        figure = fan(pars=parameters, probs=probs, historic=history, figsize=(12, 6))
        if save:
            figure.savefig(SAVE_PATH + 'fan00.png', dpi=200)
        figure = fan(pars=parameters, probs=probs, historic=history[history.Date >= '2018'])
        if save:
            figure.savefig(SAVE_PATH + 'fan01.png', dpi=200)
        figure = fan_dark(pars=parameters, probs=probs, historic=history[history.Date >= '2018'], color='cyan')
        if save:
            figure.savefig(SAVE_PATH + 'fan02.png', dpi=200)
        figure = fan(pars=parameters, probs=probs, historic=history[history.Date >= '2018'], color='teal')
        if save:
            figure.savefig(SAVE_PATH + 'fan03.png', dpi=200)
        pars = parameters.iloc[4]
        loc = pars.Mode
        sigma = pars.Uncertainty
        gamma = pars.Skewness
        figure = fan_single(loc=9.53, sigma=1.68, gamma=1.0, probs=probs, kind='pdf')
        if save:
            figure.savefig(SAVE_PATH + 'fan04.png', dpi=200)
        figure = fan_single(loc=9.53, sigma=1.68, gamma=1.0, probs=probs, kind='cdf')
        if save:
            figure.savefig(SAVE_PATH + 'fan05.png', dpi=200)
        figure = fan_single_dark(loc=loc, sigma=sigma, gamma=gamma, probs=probs, kind='cdf')
        if save:
            figure.savefig(SAVE_PATH + 'fan06.png', dpi=200)
