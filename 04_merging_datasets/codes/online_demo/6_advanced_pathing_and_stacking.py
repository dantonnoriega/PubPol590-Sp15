## online demo
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"

# ADVANCED PATHING ---------------------------------
## contructing paths using patterns
root = main_dir + "04_merging_datasets/data/"
paths0 = [root + "file_rand_" + str(v) + ".csv" for v in range(1,5)]
paths1 = [os.path.join(root, "file_rand_%s.csv") % v for v in range(1,5)]
paths2 = [root + "file_rand_%s.csv" % v for v in range(1,5)]

## super pro way
[v for v in os.listdir(root)]
[os.path.join(root,v) for v in os.listdir(root)]
[root + v for v in os.listdir(root)]
[root + v for v in os.listdir(root) if v.startswith("file_")]
[v for v in os.listdir(root) if v.startswith("file_")]
paths3 = [root + v for v in os.listdir(root) if v.startswith("file_")]

# IMPORT DATA -----------------------------------
list_of_dfs = [ pd.read_csv(v, names = ['panid', 'date', 'kwh']) for v in paths3]
len(list_of_dfs)
type(list_of_dfs)
type(list_of_dfs[0])

## assignment data
df_assign = pd.read_csv(root + "sample_assignments.csv", usecols = [0,1])

# STACK AND MERGE ----------------
df = pd.concat(list_of_dfs, ignore_index = True)
df = pd.merge(df, df_assign)

# DROPPING AND CHANGING ROW VALUES -----------------
df1 = df.copy()
df1.drop(range(0,9), inplace = True) # inplace option will change the dataframe

df['kwh'][[0,4,10]] = 3



