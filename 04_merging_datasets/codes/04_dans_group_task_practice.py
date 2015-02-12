## group task practice
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import time

main_dir = "/Users/dnoriega/Dropbox/PubPol590_Sp15/"

# ADVANCED PATHING ------------------------------------
root = main_dir + "data_sets/CER/cooked/"
paths = [os.path.join(root, v) for v in os.listdir(root) if v.startswith("File")]

# IMPORT DATA ------------------------------------
start = time.time()

## import full data set
df = pd.concat([pd.read_table(v, names = ['ID', 'date', 'kwh'], sep = " ") for v in paths], ignore_index = True)

## import subset
# df = pd.concat([pd.read_table(v, names = ['ID', 'date', 'kwh'],
#     sep = " ", skiprows = 6000000, nrows = 1500000) for v in paths], ignore_index = True)

end = time.time()
print 'total time read and stack data...', end - start, 'seconds'

## assignment data
df_assign = pd.read_csv(root + "SME and Residential allocations.csv", usecols = range(0,5))
df_assign.columns = ['ID', 'code', 'tariff', 'stimulus', 'sme']

# NEW VARS ---------------------
start = time.time()
df['hour'] = df['date'] % 100
df['day'] = (df['date'] - df['hour']) / 100
df.sort(['ID', 'date'], inplace = True)
end = time.time()
print 'total time create new variables...', end - start, 'seconds'

# EXPLORE  ----------------------
dst_day = df[df.hour > 48]['day'].unique() # get one value for each problem day
dst_day = dst_day.astype(int)
dst_hour = df[df.hour > 48]['hour'].unique() # get one value for each problem hour
dst_hour = dst_hour.astype(int)
print dst_day, dst_hour

# CLEAN --------------------------


# STACK AND MERGE --------------------
df = pd.merge(df, df_assign)
