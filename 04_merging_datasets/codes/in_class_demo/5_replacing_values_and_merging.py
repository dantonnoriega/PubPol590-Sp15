from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/dnoriega/Desktop/pubpol590_data"
csv1 = "small_data_w_missing_duplicated.csv"
csv2 = "sample_assignments.csv"

# IMPORT DATA ----------
df1 = pd.read_csv(os.path.join(main_dir, csv1), na_values = ['-', 'NA'])
df2 = pd.read_csv(os.path.join(main_dir, csv2))

# CLEAN DATA ------------
## clean df1 (to know why, do the online demo 03)
df1 = df1.drop_duplicates()
df1 = df1.drop_duplicates(['panid', 'date'], take_last = True)

## clean df2
df2[[0,1]]
df2 = df2[[0,1]] # reassigning df2 to a subset


# COPY DATAFRAMES ---------------
df3 = df2 # creates a link/reference (alter df2 DOES AFFECT df3)
df4 = df2.copy() # creating a copy (alter df2 does NOT affect df4)


# REPLACING DATA ------------------
df2.group.replace(['T', 'C'], [1, 0])
df2.group = df2.group.replace(['T', 'C'], [1, 0])


# MERGING -------------------------
pd.merge(df1, df2) # 'many-to-one' merge using the intersection. automatically finds
                    # the keys it has in common
pd.merge(df1, df2, on = ['panid']) # specify what to merge on
pd.merge(df1, df2, on = ['panid'], how = 'inner')
pd.merge(df1, df2, on = ['panid'], how = 'outer')

df5 = pd.merge(df1, df2, on = ['panid'])


# ROW BINDS AND COLUMN BINDS ---------
df2
df4

## 'row bind'
pd.concat([df2, df4]) # the defaul is to row bind
pd.concat([df2, df4], axis = 0) # same as above
pd.concat([df2, df4], axis = 0, ignore_index = True) # `ignore_index = False` is default

## 'column bind'
pd.concat([df2, df4], axis = 1)

