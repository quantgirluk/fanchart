from plot import *

parameters = BOE_PAR.copy()
history =HISTORY.copy()

probs1 = [0.05, 0.20, 0.35, 0.65, 0.80, 0.95]
fanboe(data=parameters, p=probs1, historic=history)
fanboe(data=parameters, p=probs1, historic=history[history.Date >= '2015'].iloc[::3, ])
fanboe_single(loc=1.51, sigma=1.34, gamma=0.0, p=probs1, kind='pdf')
fanboe_single(loc=1.51, sigma=1.34, gamma=0.0, p=probs1, kind='cdf')


probs2 = np.arange(0.10, 1, 0.05)
fanboe(data=parameters, p=probs2, historic=history[history.Date >= '2015'].iloc[::3, ])
fanboe_single(loc=1.51, sigma=1.34, gamma=0.0, p=probs2, kind='pdf')
fanboe_single(loc=1.51, sigma=1.34, gamma=0.0, p=probs2, kind='cdf')