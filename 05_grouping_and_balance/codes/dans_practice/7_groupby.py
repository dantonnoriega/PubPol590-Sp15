## dan's practice (groupby)
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"

# ADVANCED PATHING ------------------------------------
root = main_dir + "04_merging_datasets/data/"
paths = [os.path.join(root, v) for v in os.listdir(root) if v.startswith("file_")]

# IMPORT DATA ------------------------------------
df = pd.concat([pd.read_csv(v, names = ['panid', 'date', 'kwh']) for v in paths], ignore_index = True)

## assignment data
df_assign = pd.read_csv(root + "sample_assignments.csv", usecols = [0,1])

# STACK AND MERGE --------------------
df = pd.merge(df, df_assign)

# GROUPBY aka "split, apply, combine" -----------------------------
## see more at http://pandas.pydata.org/pandas-docs/stable/groupby.html
## say we want to group our data on a variable, like `assignment`

# split by Control/Treatment, pooled w/o time
grp1 = df.groupby(['assignment']) # split data into two grp, T and C, ignore time

# apply mean to kwh
grp1['kwh'].apply(np.mean) # pooled means of ALL data
grp1['kwh'].mean() # same but faster

%timeit -n 100 grp1['kwh'].apply(np.mean) # pooled means of ALL data
%timeit -n 100 grp1['kwh'].mean() # pooled means of ALL data


## split by control/treatment, pooled w/ time
grp2 = df.groupby(['date', 'assignment'])

# apply mean
grp2['kwh'].apply(np.mean) # pooled means of ALL data
grp2['kwh'].mean() # same but faster

%timeit -n 100 grp2['kwh'].apply(np.mean) # pooled means of ALL data
%timeit -n 100 grp2['kwh'].mean() # pooled means of ALL data

# UNSTACKING -----------
gp2 = grp2['kwh'].mean() # hierarchical series
gp2
type(gp2)
gp2_df = gp2.unstack('assignment') # hierarchical dataframe, unstacked with 'C' and 'T' as columns
gp2_df
type(gp2_df)

# TESTING FOR BALANCE --------------------------------
from scipy.stats import ttest_ind
from scipy.special import stdtr

# TWO SAMPLE T-TEST ---------------------------------
## POOLED
trt = df['kwh'][df.assignment == 'T'] # get pooled data of treatment group
ctrl = df['kwh'][df.assignment == 'C'] # get pooled data of control group
t, p = ttest_ind(trt, ctrl, equal_var=False) # do means comparison, assuming NO equal variance
t # t statistic
p # pvalue

## OVERTIME
grp = df.groupby(['date', 'assignment']) # create groupby object

trt = { k[0]: df.kwh[v].values for k, v in grp.groups.iteritems() if k[1] == 'T'} # get set of all treatments by date
ctrl = { k[0]: df.kwh[v].values for k, v in grp.groups.iteritems() if k[1] == 'C'} # get set of all controls by date
keys = ctrl.keys()
diff = { k : (trt[k].mean() - ctrl[k].mean()) for k in keys}
tstats = { k : float(ttest_ind(trt[k], ctrl[k], equal_var = False)[0]) for k in keys } # get t stats of two sample t test
pvals = { k : ttest_ind(trt[k], ctrl[k])[1] for k in keys } # get p values
tstats_pvals = { k : (tstats[k], pvals[k]) for k in keys }

## MultiIndex
cols = [col for col in df.columns if col not in ['kwh']]
tuples = [tuple(v) for v in df[cols].values]
index = pd.MultiIndex.from_tuples(tuples)
kwh = Series(df.kwh, index = index)

