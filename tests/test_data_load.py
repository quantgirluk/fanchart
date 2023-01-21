from fanchart import load_boe_parameters, load_boe_history
import pandas as pd

parameters = load_boe_parameters()
history = load_boe_history()


def test_load_parameters():
    assert parameters.shape == (13, 4)
    modes = [9.93,
             13.1,
             12.56,
             10.79,
             9.53,
             5.46,
             4.33,
             2.64,
             2,
             1.4,
             1.16,
             0.93,
             0.76]
    for m1, m2 in zip(parameters.Mode, modes):
        assert m1 == m2


def test_load_history():
    assert history.shape == (74, 2)
    cpis = [1.3,
            1.4,
            1.3,
            1.4,
            1.7,
            2,
            2.4,
            2.1,
            1.9,
            2.3,
            2.4,
            2.7,
            2.9,
            2.6,
            1.8,
            2.1,
            2.4,
            3.4,
            4.8,
            3.9,
            3,
            2.1,
            1.5,
            2.1,
            3.3,
            3.5,
            3.1,
            3.4,
            4.1,
            4.4,
            4.7,
            4.6,
            3.5,
            2.8,
            2.4,
            2.7,
            2.8,
            2.7,
            2.7,
            2.1,
            1.7,
            1.7,
            1.5,
            0.9,
            0.1,
            0,
            0,
            0.1,
            0.3,
            0.4,
            0.7,
            1.2,
            2.1,
            2.7,
            2.8,
            3,
            2.7,
            2.4,
            2.5,
            2.3,
            1.9,
            2,
            1.8,
            1.4,
            1.7,
            0.6,
            0.6,
            0.5,
            0.6,
            2.1,
            2.8,
            4.9,
            6.2,
            9.2]
    for v1, v2 in zip(history.Inflation, cpis):
        assert v1 == v2
