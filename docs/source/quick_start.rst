Quick-Start Guide
=================

This guide explains how to use the library `fanchart` to create charts as those included in the Monetary Policy Report produced by tge Bank of England (BoE).

Load Historical Data
--------------------

We start by loading the data required to make the charts with the functions

 - `load_boe_history()` which loads the historical data for inflation (CPI)
 - `load_boe_parameters()` which loads the parameters for the quarterly projections

 Both data sets correspond to the Monetary Policy Report - August 2022

.. code-block:: python

    from fanchart import load_boe_history, load_boe_parameters

    parameters = load_boe_parameters()
    history = load_boe_history()


Make your first Fan Chart
-------------------------

To make our first fan chart we use the ``fan`` function which requires three parameters


- pars    : The parameters to be used for the quarterly forecasts. We can use the parameters previosly loaded
- probs   : The probabilities that define the bands in the fan chart. This should be a sequence of increasing probabilities in an araray type format.
- history : The historical values of the CPI inflation. We can use the parameters previously loaded

.. code-block:: python

    from fanchart import fan

    probs = [0.05, 0.20, 0.35, 0.65,0.80,  0.95]
    fan(pars=parameters, probs=probs, historic=history)



.. image:: _static/fan00.png

The results is a plot showing

- The historical (observed) values of the CPI inflation from 2004 until a quarter before the projection starts.
- Then, the "fan" part is shown in a shadowed area and labeled as projection. This part illustrates the forecasted distribution for 13 quarters from the last observed value.

We can restrict the data in the history part to show only the data that we want.
For example, in the following fan chart we show only yearly data from 2018.


.. code-block:: python

    from fanchart import fan

    probs = [0.05, 0.20, 0.35, 0.65,0.80,  0.95]
    fan(pars=parameters, probs=probs, historic=history[history.Date >= '2018'])

.. image:: _static/fan01.png


Single Quarter Fan Charts
--------------------------

The fanchart package also provides functionality to visualise each of the quarterly forecast on its own.
This is achieved by the function `fan_single` which requires the following parameters:

- loc   : Locantion parameter (Mode)
- sigma : Uncertainty parameter
- gamma : Skewness parametere
- probs : A set of probabilities
- kind  : A string either 'pdf' or 'cdf' to define the type of plot

We can plot the forecasted probability density function as follows.

.. code-block:: python

    from fanchart import fan_single

    probs = [0.05, 0.20, 0.35, 0.65,0.80,  0.95]
    fan_single(loc=9.53, sigma=1.68, gamma=1.0, probs=probs, kind='pdf')


.. image:: _static/fan04.png

Similarly, we can plot the forecasted cumulative probability function.

.. code-block:: python

    from fanchart import fan_single

    probs = [0.05, 0.20, 0.35, 0.65,0.80,  0.95]
    fan_single(loc=9.53, sigma=1.68, gamma=1.0, probs=probs, kind='cdf')


.. image:: _static/fan05.png
