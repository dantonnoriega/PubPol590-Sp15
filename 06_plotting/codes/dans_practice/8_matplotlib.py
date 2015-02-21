## dan's practice (matplotlib)
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"

# ADVANCED PATHING ------------------------------------
root = main_dir + "05_grouping_and_balance/data/"
paths = [os.path.join(root, v) for v in os.listdir(root) if v.startswith("file_")]

# IMPORT DATA ------------------------------------
df = pd.concat([pd.read_csv(v, names = ['panid', 'date', 'kwh'],
    header = None, parse_dates = [1]) for v in paths], ignore_index=True) # ensure we parse dates

## assignment data
df_assign = pd.read_csv(root + "sample_assignments.csv", usecols=[0, 1])

## STACK AND MERGE --------------------
df = pd.merge(df, df_assign)

## OVER-TIME -------------------------------
from scipy.stats import ttest_ind

grp = df.groupby(['date', 'assignment']) # create groupby object

## split up treatment/control
trt = {k[0]: df.kwh[v].values for k, v in grp.groups.iteritems() if k[1] == 'T'} # get set of all treatments by date
ctrl = {k[0]: df.kwh[v].values for k, v in grp.groups.iteritems() if k[1] == 'C'} # get set of all controls by date
keys = ctrl.keys()

# ## get diff in means, tstats, and pvals
# diff = {k: (trt[k].mean() - ctrl[k].mean()) for k in keys}
# tstats = {k: float(ttest_ind(trt[k], ctrl[k], equal_var=False)[0]) for k in keys} # get t stats of two sample t test
# pvals = {k: ttest_ind(trt[k], ctrl[k])[1] for k in keys} # get p values
# tstats_pvals = {k: (tstats[k], pvals[k]) for k in keys}

## better yet, make dfs!
tstats = DataFrame([(k, np.abs(float(ttest_ind(trt[k], ctrl[k], equal_var=False)[0]))) for k in keys],
    columns = ['date', 'tstat']) # get t stats of two sample t test
pvals = DataFrame([(k, ttest_ind(trt[k], ctrl[k])[1]) for k in keys],
    columns = ['date', 'pval']) # get t stats of two sample t test
t_p = pd.merge(tstats, pvals)

## sort and reset index
t_p.sort(['date'], inplace=True)
t_p.reset_index(inplace=True, drop=True)

## GRAPH ---------------------------------

fig1 = plt.figure() # intialize a figure
ax1 = fig1.add_subplot(2,1,1)   # create a 2x1 (RxC) matrix, first panel to ax1
ax1.plot(t_p['tstat'])  # plot data (x axis is index)
ax1.axhline(2, color='r', linestyle='--') # add horizontal lines with .axhline (vertical with .axvline)
ax1.set_title('t-stats over-time') # set title
ax2 = fig1.add_subplot(2,1,2)  # second panel to ax2
ax2.plot(t_p['pval'])
ax2.axhline(0.05, color='r', linestyle='--')
ax2.set_title('p-values over-time')
plt.show()
