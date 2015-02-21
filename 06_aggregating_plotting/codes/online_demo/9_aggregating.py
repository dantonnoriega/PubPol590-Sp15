from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"
root = main_dir + "06_aggregating_plotting/data/"

# IMPORT AND MERGE DATA ---------------
df = pd.read_csv(root + "sample_30min.csv", header=0, parse_dates=[1])
df_assign = pd.read_csv(root + 'sample_assignments.csv', usecols=[0,1])

df = pd.merge(df, df_assign)

# NEW VARIABLES ------------------
df['year'] = df['date'].apply(lambda x: x.year)
df['month'] = df['date'].apply(lambda x: x.month)
df['day'] = df['date'].apply(lambda x: x.day)

# AGGREGATION (DAILY) ---------------
grp = df.groupby(['year', 'month', 'day', 'panid', 'assignment'])
agg = grp['kwh'].sum()

# reset index
agg = agg.reset_index()
grp1 = agg.groupby(['year', 'month', 'day', 'assignment'])

# split up T/C
trt = {(k[0], k[1], k[2]): agg.kwh[v].values 
    for k, v in grp1.groups.iteritems() if k[3] == 'T'}
ctrl = {(k[0], k[1], k[2]): agg.kwh[v].values 
    for k, v in grp1.groups.iteritems() if k[3] == 'C'}
keys = ctrl.keys()

# tstats and pvals
tstats = DataFrame([(k, np.abs(float(ttest_ind(trt[k], ctrl[k], equal_var=False)[0])))
    for k in keys], columns=['ymd', 'tstat'])
pvals = DataFrame([(k, (ttest_ind(trt[k], ctrl[k], equal_var=False)[1]))
    for k in keys], columns=['ymd', 'pval'])
t_p = pd.merge(tstats, pvals)

# sort and reset
t_p.sort(['ymd'], inplace=True)
t_p.reset_index(inplace=True, drop=True)


# PLOTTING ----------------------------
fig1 = plt.figure() # initialize plot
ax1 = fig1.add_subplot(2,1,1) # two rows, one column, first plot
ax1.plot(t_p['tstat'])
ax1.axhline(2, color='r', linestyle='--')
ax1.axvline(14, color='g', linestyle='--')
ax1.set_title('t-stats over-time')

ax2 = fig1.add_subplot(2,1,2) # two rows, one column, first plot
ax2.plot(t_p['pval'])
ax2.axhline(0.05, color='r', linestyle='--')
ax2.axvline(14, color='g', linestyle='--')
ax2.set_title('p-values over-time')
plt.show()