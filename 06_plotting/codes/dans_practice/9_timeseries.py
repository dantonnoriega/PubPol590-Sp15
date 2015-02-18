## group task practice
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import time
import matplotlib.pyplot as plt
import pytz
from datetime import datetime, timedelta


main_dir = "/Users/dnoriega/Dropbox/PubPol590_Sp15/"

# ADVANCED PATHING ------------------------------------
root = main_dir + "data_sets/CER/cooked/"
paths = [os.path.join(root, v) for v in os.listdir(root) if v.startswith("File")]

# IMPORT DATA ------------------------------------
start = time.time()

## import full data set
df = pd.concat([pd.read_table(v, names = ['ID', 'date_cer', 'kwh'], sep = " ") for v in paths], ignore_index = True)

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
df['hour_cer'] = df['date_cer'] % 100
df['day_cer'] = (df['date_cer'] - df['hour_cer']) / 100
df.sort(['ID', 'date_cer'], inplace = True)
end = time.time()
print 'total time create new variables...', end - start, 'seconds'


# MERGE ASSIGNMENT --------------------

start = time.time()
df = pd.merge(df, df_assign)
end = time.time()
print 'total time to merge assignment...', end - start, 'seconds'


# TRIM --------------------------
## keep residential only (`code == 1`)
df = df[df['code'] == 1]

## keep only `stimulus == 1 | stimulus == E | tariff == A` (one treatment type and control)
df[(df['stimulus'] == '1') | (df['stimulus'] == 'E') | (df['tariff'] == 'A')]




# MERGE TIMESERIES ---------------------


# full merge
start = time.time()
df = pd.merge(df, df_assign)
df = pd.merge(df, df_ts, on = ['day_cer', 'hour_cer'], how = 'inner')
end = time.time()
print 'total time to merge...', end - start, 'seconds'

# df2 = df[~df['ID'].isnull()]
