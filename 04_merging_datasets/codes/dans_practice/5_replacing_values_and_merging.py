from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/dnoriega/Dropbox/pubpol590_sp15/data_sets/"
csv1 = "L4/small_data_w_missing_duplicated.csv"
csv2 = "L4/sample_assignments.csv"


# IMPORT DATA ---------------------------------------
df1 = pd.read_csv(os.path.join(main_dir, csv1), na_values = ['-', 'NA'])
df2 = pd.read_csv(os.path.join(main_dir, csv2))

# CLEAN DATA ------------------------------
## clean df1
df1 = df1.drop_duplicates() # drop dups
df1 = df1.drop_duplicates(['panid', 'date'], take_last = True) # this will keep the bottom to top

## clean df2
df2[[0,1]]
df2 = df2[[0,1]] # keep only first two columns
df2



# CREATING COPIES ----------------------------
## creating copies
df3 = df2 # this will NOT copy, but make a reference i.e. changing df2 will change df3
df4 = df2.copy() # creates a new copy of df2 and assign to df4. changing df2 will NOT affect df4



# REPLACING DATA --------------------------------
## use `replace` to replaces values but without changing original data set
df2.group.replace(["T", "C"], [1, 0])
df2 # unchanged
df2.group = df2.group.replace(["T", "C"], [1, 0]) # have to assign for change to hold
df2

## check df3 and df4
df3 # df2 changed so df3 changed as well, since it was referenced, not copied
df4 # df4 is unchanged

## can also use `map` to replace values as well
new_lbls = {'T': 'TREATED', 'C': 'CONTROL'}
df4.group.map(new_lbls)
df4.group = df4.group.map(new_lbls)
df4


# MERGING ----------------------------------------
## default merge is 'many-to-one' using the intersection of the datasets i.e. the 'inner' join
## notice that in both merges, it excludes `panid == 5`. this is due to 'inner'
pd.merge(df1, df2) # pandas will automatically find the keys each dataframe has in common and do 'inner' merge
pd.merge(df1, df2, on = 'panid') # attaching df2 to df1 on value 'panid'

## if we want to keep all values from BOTH data sets, we use the `how = 'outer'` option
pd.merge(df1, df2, on = 'panid', how = 'outer') # notice how it keeps the `panid == 5`


# COMBINING AND STACKING with `pd.concat` aka row and column binds --------------------
df2
df4

## the default is a "row bind" or "stacking"
pd.concat([df2, df4]) # note: must pass as list
pd.concat([df2, df4], axis = 0) # option `axis = 0` is the default, where 0 is 'row'
pd.concat([df2, df4], axis = 1) # option `axis = 1` is a 'column bind'
pd.concat([df2, df4], axis = 0, ignore_index = True) # `ignore_index = True` will reset the index


