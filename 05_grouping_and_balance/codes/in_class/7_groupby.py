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

# split by C/T, pooled w/o time
groups1 = df.groupby(['assignment']) # splitting by assignment
groups1.groups

# apply the mean
groups1['kwh'].apply(np.mean) # .apply is to 'apply' ANY type of function
groups1['kwh'].mean() # .mean() is an internal method (faster)

%timeit -n 100 groups1['kwh'].apply(np.mean) # .apply is to 'apply' ANY type of function
%timeit -n 100 groups1['kwh'].mean() # .mean() is an internal method (faster)


# split by C/T, pooling w time
groups2 = df.groupby(['date','assignment']) # splitting by assignment

# apply the mean
groups2['kwh'].mean() # .mean() is an internal method (faster)


# UNSTACK -----------

gp_mean = groups2['kwh'].mean()
gp_unstack = gp_mean.unstack('assignment')
gp_unstack['T'] # mean, over time, of all treated panids


