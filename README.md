# *fanchart* 


[![PyPI version fury.io](https://badge.fury.io/py/fanchart.svg)](https://pypi.python.org/pypi/fanchart/)
![PyPI license](https://img.shields.io/pypi/l/fanchart.svg)

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

## Quick Start
This library provides two main functions

| Function    | Parameters                            |
|-------------|---------------------------------------|
| fan _single | loc, sigma, gamma, probs, kind, color |
| fan         | pars, probs, historic, color          |



- The `fan` function illustrates the distribution of all the forecasts available; and it has the option to display the historical values for reference.

![](https://raw.githubusercontent.com/quantgirluk/fanchart/master/images/fan_light.png)


- The `fan_single` function illustrates the pdf/cdf of one forecast distribution

![](https://raw.githubusercontent.com/quantgirluk/fanchart/master/images/single_light.png)

![](https://raw.githubusercontent.com/quantgirluk/fanchart/master/images/single_light_cdf.png)

## Thanks for Visiting! ✨

Connect with me via:

- 🦜 [Twitter](https://twitter.com/Quant_Girl)
- 👩🏽‍💼 [Linkedin](https://www.linkedin.com/in/dialidsantiago/)
- 📸 [Instagram](https://www.instagram.com/quant_girl/)
- 👾 [Personal Website](https://quantgirl.blog)


⭐️ **If you like this projet, please give it a star!** ⭐️
