## dan's practice (aggregating)
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"

# ADVANCED PATHING ------------------------------------
root = main_dir + "06_aggregating_plotting/data/"

# IMPORT DATA ------------------------------------
df = pd.read_csv(root + "sample_30min.csv", header=0, parse_dates = [1])
df_assign = pd.read_csv(root + "sample_assignments.csv", usecols = [0,1])

# MERGE ---------
df = pd.merge(df, df_assign)

# ADD/DROP VARIABLES ---------------------------
df['year'] = df['date'].apply(lambda x: x.year)
df['month'] = df['date'].apply(lambda x: x.month)
df['day'] = df['date'].apply(lambda x: x.day) # x.day returns integer; x.date() returns date object
df['ymd'] = df['date'].apply(lambda x: x.date()) # notice the parentheses in `.date()`

# DAILY AGGREGATION --------------------
grp = df.groupby(['ymd', 'panid', 'assignment'])
agg = grp['kwh'].sum()

# reset the index (multilevel at the moment)
agg = agg.reset_index() # drop the multi-index
grp = agg.groupby(['ymd', 'assignment'])

## split up treatment/control
trt = {k[0]: agg.kwh[v].values for k, v in grp.groups.iteritems() if k[1] == 'T'} # get set of all treatments by date
ctrl = {k[0]: agg.kwh[v].values for k, v in grp.groups.iteritems() if k[1] == 'C'} # get set of all controls by date
keys = ctrl.keys()

## better yet, make dfs!
tstats = DataFrame([(k, np.abs(float(ttest_ind(trt[k], ctrl[k], equal_var=False)[0]))) for k in keys],
    columns = ['yd', 'tstat']) # get t stats of two sample t test
pvals = DataFrame([(k, ttest_ind(trt[k], ctrl[k])[1]) for k in keys],
    columns = ['yd', 'pval']) # get t stats of two sample t test
t_p = pd.merge(tstats, pvals)

## sort and reset index
t_p.sort(['yd'], inplace=True)
t_p.reset_index(inplace=True, drop=True)


# PLOTTING ----------------------------
fig1 = plt.figure() # initialize plot
ax1 = fig1.add_subplot(2,1,1) # two rows, one column, first plot
ax1.plot(t_p['tstat'])
ax1.axhline(2, color='r', linestyle='--')
ax1.set_title('t-stats over-time')

ax2 = fig1.add_subplot(2,1,2) # two rows, one column, first plot
ax2.plot(t_p['pval'])
ax2.axhline(0.05, color='r', linestyle='--')
ax2.set_title('p-values over-time')
plt.show()