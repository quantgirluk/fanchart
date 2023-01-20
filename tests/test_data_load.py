from fanchart import load_boe_parameters, load_boe_history
import pandas as pd

parameters = load_boe_parameters()
history = load_boe_history()

def test_load_parameters():

    par_static = pd.read_csv('../fanchart/data/fan_parameters_2022Q3.csv')
    assert par_static.shape == parameters.shape
    assert par_static.equals(parameters)

def test_load_history():

    hist_static = pd.read_csv('../fanchart/data/fan_history_2022Q3.csv')
    assert hist_static.shape == history.shape
    assert hist_static.equals(history)

