# *fanchart* 

[![PyPI version fury.io](https://badge.fury.io/py/fanchart.svg)](https://pypi.python.org/pypi/fanchart/)
[![Downloads](https://static.pepy.tech/personalized-badge/fanchart?period=total&units=international_system&left_color=black&right_color=blue&left_text=Downloads)](https://pepy.tech/project/fanchart)

![PyPI license](https://img.shields.io/pypi/l/fanchart.svg)
![example workflow](https://github.com/quantgirluk/fanchart/actions/workflows/python-package.yml/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/fanchart/badge/?version=latest)](https://fanchart.readthedocs.io/en/latest/?badge=latest)


- [Documentation](https://fanchart.readthedocs.io/en/latest/)
- [Git Homepage](https://github.com/quantgirluk/fanchart)
- [Pip Repository](https://pypi.org/project/fanchart/)

## Overview

The **_fanchart_** library provides functionality to create fan charts in [Python](https://www.python.org/).


The term **fan chart** was coined by the [Bank of England](https://www.bankofengland.co.uk/) in 1996. Since then, the  BoE 
has used these charts to illustrate its forecasts for inflation.

The BoE introduced the fan charts aiming to communicate a more accurate representation of their forecast for medium term inflation. In particular, the charts have two key objectives:

- To convey the uncertainty in their forecasts. This is, to focus attention on  the forecast distribution, rather than only on small changes to the central projection.
- To promote discussion of the risks to the economic outlook, and thus contribute to a wider debate about economic policy. Fan charts help to make it clear that monetary policy is about making decisions instead of knowing the exact rate of inflation in two years time.

For more details on the history of fan charts visit [Fan Charts](https://quantgirl.blog/fan-charts/)


## Installation


Fanchart is available on [pypi](https://pypi.org/project/fanchart/) and can be
installed as follows.


```
pip install fanchart
```

## Dependencies

Fanchart relies heavily on

- [``twopiece``](https://pypi.org/project/twopiece/)  for the implementation of the [Two-Piece normal](https://quantgirl.blog/two-piece-normal/) distribution

- ``matplotlib`` for creating visualisations

## Compatibility


Fanchart is tested on Python versions 3.8, 3.9, and 3.10


## Getting Started

This library provides two main functions `fan` and `fan_single`. In order to be able to make our first fan charts with 
these functions, we need to load some data via the functions.

- ``load_boe_history()`` which loads the historical data for inflation (CPI)
- ``load_boe_parameters()`` which loads the parameters for the quarterly projections

```
from fanchart import load_boe_history, load_boe_parameters

history = load_boe_history()
parameters = load_boe_parameters()
```

After this, we are ready to use our main functions.

- The `fan` function illustrates the distribution of all the forecasts available; and it has the option to display the historical values for reference.

```
    from fanchart import fan

    probs = [0.05, 0.20, 0.35, 0.65,0.80,  0.95]
    fan(pars=parameters, probs=probs, historic=history[history.Date >= '2018'])
```


![](https://raw.githubusercontent.com/quantgirluk/fanchart/master/docs/source/_static/fan01.png)


- The `fan_single` function illustrates the pdf/cdf of one forecast distribution

```
    from fanchart import fan_single

    probs = [0.05, 0.20, 0.35, 0.65,0.80,  0.95]
    fan_single(loc=9.53, sigma=1.68, gamma=1.0, probs=probs, kind='pdf')

```

![](https://raw.githubusercontent.com/quantgirluk/fanchart/master/docs/source/_static/fan04.png)

```
    from fanchart import fan_single

    probs = [0.05, 0.20, 0.35, 0.65,0.80,  0.95]
    fan_single(loc=9.53, sigma=1.68, gamma=1.0, probs=probs, kind='cdf')
```



![](https://raw.githubusercontent.com/quantgirluk/fanchart/master/docs/source/_static/fan05.png)

## Thanks for Visiting! ✨

Connect with me via:

- 🦜 [Twitter](https://twitter.com/Quant_Girl)
- 👩🏽‍💼 [Linkedin](https://www.linkedin.com/in/dialidsantiago/)
- 📸 [Instagram](https://www.instagram.com/quant_girl/)
- 👾 [Personal Website](https://quantgirl.blog)


⭐️ **If you like this projet, please give it a star!** ⭐️
