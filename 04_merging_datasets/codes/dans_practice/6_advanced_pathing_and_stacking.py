## dan's practice
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"

# ADVANCED PATHING ------------------------------------
## making a list of file paths using loops
# we want to import files 'file_rand_1' to 'file_rand_4'. note the pattern of 'file_rand_i' where i = 1 - 4
# we can make a list of file names by combining strings based on the pattern.
root = main_dir + "04_merging_datasets/data/"
paths0 = [ root + "file_rand_" + str(v) + ".csv" for v in range(1,5) ]
paths1 = [ os.path.join(root, "file_rand_%s.csv") % v for v in range(1,5) ]
paths2 = [ (root + "file_rand_%s.csv") % v for v in range(1,5) ]

## super pro way
[ v for v in os.listdir(root) ]
[ v for v in os.listdir(root) if v.startswith("file_") ]
[ os.path.join(root, v) for v in os.listdir(root) if v.startswith("file_") ]
paths3 = [ os.path.join(root, v) for v in os.listdir(root) if v.startswith("file_") ]

# IMPORT DATA ------------------------------------
# create list of DataFrames
## VERY IMPORTANT to name the dataframe. need keys to stack.
list_of_dfs = [ pd.read_csv(v, names = ['panid', 'date', 'kwh']) for v in paths3]
len(list_of_dfs)
type(list_of_dfs)
type(list_of_dfs[0])

## assignment data
df_assign = pd.read_csv(root + "sample_assignments.csv", usecols = [0,1])
# OR
df_assign = pd.read_csv(root + "sample_assignments.csv")
df_assign = df_assign[[0,1]]

# STACK AND MERGE --------------------
df = pd.concat(list_of_dfs, ignore_index = True)
df = pd.merge(df, df_assign)

# DROPPING AND CHANGING ROW VALUES -----------------
df.drop(range(0,9), inplace = True) # inplace option will change the dataframe
df['kwh'][10] = 3