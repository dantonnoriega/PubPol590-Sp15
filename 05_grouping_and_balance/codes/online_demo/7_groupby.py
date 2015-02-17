from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"
root = main_dir + "05_grouping_and_balance/data/"

# PATHING --------------
paths = [os.path.join(root,v) for v in os.listdir(root) if v.startswith("file_")]

# IMPORT AND STACK ---------
df = pd.concat([pd.read_csv(v, names = ['panid', 'date', 'kwh']) for v in paths],
    ignore_index = True)
    
df_assign = pd.read_csv(root + "sample_assignments.csv", usecols = [0,1])

# MERGE ---------
df = pd.merge(df, df_assign)

# GROUPBY aka "split, apply, combine"
## see more at http://pandas.pydata.org/pandas-docs/stable/groupby.html
grp1 = df.groupby(['assignment']) # .groupby objects for big data
gd1 = grp1.groups # CAUTION! don't do this with super big data. it will crash.

## peek inside gd1 (dictionary)
gd1.keys()
gd1['C'] # gd1 is a dict, so must use keys to get data
gd1.values()[0] # gd1.values() is a list, so we can use numerical indeces
gd1.viewvalues() # see all the values of the dictionary, gd1

## iteration properties of a dictionary
[v for v in gd1.itervalues()]
gd1.values() # equivalent to above

[k for k in gd1.iterkeys()]
gd1.keys() # equivalent

[(k,v) for k,v in gd1.iteritems()]
gd1

## split and apply (pooled data)
grp1['kwh'].mean()

## split and apply (panel/time series data)
grp2 = df.groupby(['assignment','date'])
gd2 = grp2.groups
gd2 # look at the dictionary (key, value) pairs
grp2['kwh'].mean() 


## TESTING FOR BALANCE (OVER-TIME)
from scipy.stats import ttest_ind
from scipy.special import stdtr

## ex using ttest_ind
a = [1, 4, 9, 2]
b = [1, 7, 8, 9]

t, p = ttest_ind(a, b, equal_var = False)


# set up data
grp = df.groupby(['assignment', 'date'])

# get separate sets of treatment and control values by date
trt = {k[1]: df.kwh[v].values for k, v in grp.groups.iteritems() if k[0] == 'T'}
ctrl = {k[1]: df.kwh[v].values for k, v in grp.groups.iteritems() if k[0] == 'C'}
keys = trt.keys()

# comparisons!
diff = {k: (trt[k].mean() - ctrl[k].mean()) for k in keys}
tstats = {k: float(ttest_ind(trt[k], ctrl[k], equal_var = False)[0]) for k in keys}
pvals = {k: float(ttest_ind(trt[k], ctrl[k], equal_var = False)[1]) for k in keys}
t_p = {k: (tstats[k], pvals[k]) for k in keys}
