# get subsample of data
# Tariff A and B, stimuli 1 and 3, all control

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
from scipy.stats import ttest_ind


main_dir = "/Users/dnoriega/Dropbox/PubPol590_Sp15/"

# ADVANCED PATHING ------------------------------------
root = main_dir + "data_sets/CER/cooked/"
paths = [os.path.join(root, v) for v in os.listdir(root) if v.startswith("File")]

# IMPORT DATA ------------------------------------
## import ONLY ids [first column] from each file
start = time.time()
df = pd.concat([pd.read_table(v, names = ['ID', 'date_cer', 'kw'], sep = " ") for v in paths], ignore_index = True)
end = time.time()
print 'total time read and stack data...', end - start, 'seconds'

## assignment data
df_assign = pd.read_csv(root + "SME and Residential allocations.csv", usecols=range(0,4))
df_assign.columns = ['ID', 'code', 'tariff', 'stimulus']

## time data
df_time = pd.read_csv(root + "timeseries_correction.csv", parse_dates = [0, 1])
df_time['ts'] = df_time['ts'].apply(np.datetime64)
df_time['date'] = df_time['date'].apply(np.datetime64)

## create trial variable
df_time['trial'] = 0 + (df_time['year'] > 2009)
df_time = df_time[df_time['date'] >= np.datetime64('2009-07-01', 'D')]
# df_time.to_csv(main_dir + 'data_sets/CER/tasks/time_correction.csv', index = False)


# TRIM --------------------------
## keep residential only (`code == 1`)
df_assign = df_assign[df_assign['code'] == 1]

## keep tariff A and B and simuli 1 and 3 plus control
tariffs = ['A', 'B']
stimuli = ['1', '3']

# find tariff subsample then, from that subsample, find stimuli matches
indx_1 = [k for k, v in df_assign['tariff'].iteritems() if any(v == j for j in tariffs)]
indx = [k for k, v in df_assign['stimulus'].loc[indx_1].iteritems() if any(v == j for j in stimuli)]

# EXTRACT AND STACK --------------------------
# use index label location the stack
# more info here: http://stackoverflow.com/questions/20838395/what-is-the-point-of-ix-indexing-for-pandas-series)
df_T = df_assign.loc[indx, :]
df_C = df_assign[(df_assign['stimulus'] == 'E')]
df_TC = pd.concat([df_C, df_T], ignore_index = True)

# find xtab freq counts
df_TC[['tariff', 'stimulus']].pivot_table(rows = 'tariff', cols = ['stimulus'], aggfunc=len, fill_value = 0)


# MERGE ASSIGNMENTS ----------------------
df_redux = pd.merge(df, df_TC)

# NEW VARS ---------------------
start = time.time()
df_redux['hour_cer'] = df_redux['date_cer'] % 100
df_redux['day_cer'] = (df_redux['date_cer'] - df_redux['hour_cer']) / 100
df_redux['kwh'] = df_redux['kw']/2
df_redux.reset_index(inplace=True)
end = time.time()
print 'total time create new variables...', end - start, 'seconds'


# MERGE TIME ---------------------
df_time_pretrial = df_time[df_time['trial']==0]
df_redux_pretrial = pd.merge(df_redux, df_time_pretrial)
df_redux_pretrial = df_redux_pretrial[['ID', 'kwh', 'year', 'month', 'day', 'hour', 'minute']]


# EXPORT DATA ---------------------
df_TC.to_csv(main_dir + 'data_sets/CER/tasks/allocation_subsamp.csv', index=False)
# df_redux.to_csv(main_dir + 'data_sets/CER/tasks/kwh_redux.csv', index=False)
df_redux_pretrial.to_csv(main_dir + 'data_sets/CER/tasks/kwh_redux_pretrial.csv', index=False)

