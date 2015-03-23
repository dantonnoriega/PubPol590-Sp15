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

## import full data set
start = time.time()
df = pd.concat([pd.read_table(v, names = ['ID', 'date_cer', 'kwh'], sep = " ") for v in paths], ignore_index = True)
end = time.time()
print 'total time read and stack data...', end - start, 'seconds'

## assignment data
df_assign = pd.read_csv(root + "SME and Residential allocations.csv", usecols = range(0,5))
df_assign.columns = ['ID', 'code', 'tariff', 'stimulus', 'sme']

# TRIM --------------------------
## keep residential only (`code == 1`)
df_assign = df_assign[df_assign['code'] == 1]

## keep only `stimulus == 1 | stimulus == E | tariff == A` (one treatment type and control)
df_assign = df_assign[(df_assign['stimulus'] == 'E') | ((df_assign['tariff'] == 'A') & (df_assign['stimulus'] == '1'))]


# MERGE ASSIGNMENT --------------------
start = time.time()
df = pd.merge(df, df_assign)
end = time.time()
print 'total time to merge assignment...', end - start, 'seconds'


# NEW VARS ---------------------
start = time.time()
df['hour_cer'] = df['date_cer'] % 100
df['day_cer'] = (df['date_cer'] - df['hour_cer']) / 100
df.sort(['date_cer', 'ID'], inplace = True)
df.reset_index(inplace=True)
end = time.time()
print 'total time create new variables...', end - start, 'seconds'



# TIMESERIES CORRECTION -----------------------------------
start = time.time()

tz = pytz.timezone('Europe/Dublin') # this is the timezone smart meters are in
start_datetime = tz.localize(datetime(2009, 1, 1, 0, 0, 0), is_dst = True) # start date of experiment
end_datetime = tz.localize(datetime(2011, 1, 1, 0, 0, 0) - timedelta(minutes=30), is_dst= True) # end date of experiment

# fill in an empty list with the DST corrected dates
d = start_datetime
ts = [d]

while d < end_datetime:
    # print str(d) + ' ' + d.tzname()
    d = tz.normalize(d + timedelta(minutes=30))  # Add 30 minutes
    ts.append(d)

ts = pd.to_datetime(ts) # convert to np.ndarray
tznames = [v.tzname() for v in ts]

## create a DataFrame to link corrected time data with actual data in 'df'
df_ts = pd.DataFrame(zip(ts, ts.date, ts.year, ts.month, ts.day, ts.hour, ts.minute, tznames),
    columns=['ts', 'date', 'year', 'month', 'day', 'hour', 'minute', 'tz'])

df_ts['hour_cer'] = df_ts.groupby('date').cumcount() + 1 # create a counter that span the 30 min intervals


# link dates to cer day
cer_day_link = DataFrame({'date': pd.unique(df_ts['date'])}) # find all unique dates
cer_day_link['day_cer'] = cer_day_link.index + 1 # link dates to the day counter (just index + 1)

# merge the dataframe, linking the CER format to DST corrected time values
df_ts = pd.merge(df_ts, cer_day_link, on='date')

# CER ANOMOLY CORRECTION
## see http://pandas.pydata.org/pandas-docs/stable/indexing.html#advanced-indexing-with-labels
df_ts.ix[df_ts['day_cer'] == 452, 'hour_cer'] = np.array([v for v in range(1,49) if v not in [2,3]])

end = time.time()
print 'total time series correction...', end - start, 'seconds'


# MERGE TIMESERIES ---------------------
start = time.time()
df = pd.merge(df, df_ts, on=['day_cer', 'hour_cer'], how='inner')
end = time.time()
print 'total time to merge time series...', end - start, 'seconds'


# ADD/DROP VARIABLES ---------------------------
df.drop(['sme'], inplace=True, axis=1)
df['assignment'] = 0 + (df['tariff'] != 'E')


# MONTHLY AGGREGATION --------------------
grp = df.groupby(['year', 'month', 'ID', 'assignment']) # aggregate over date, ID, and keep assignments
agg = grp['kwh'].sum()

# reset the index (multilevel at the moment)
agg = agg.reset_index() # drop the multi-index
grp = agg.groupby(['year', 'month', 'assignment'])

## split up treatment/control
trt = {(k[0], k[1]): agg.kwh[v].values for k, v in grp.groups.iteritems() if k[2] == 1} # get set of all treatments by date
ctrl = {(k[0], k[1]): agg.kwh[v].values for k, v in grp.groups.iteritems() if k[2] == 0} # get set of all controls by date
keys = ctrl.keys()

## better yet, make dfs!
tstats = DataFrame([(k, np.abs(float(ttest_ind(trt[k], ctrl[k], equal_var=False)[0]))) for k in keys],
    columns = ['ym', 'tstat']) # get t stats of two sample t test
pvals = DataFrame([(k, ttest_ind(trt[k], ctrl[k])[1]) for k in keys],
    columns = ['ym', 'pval']) # get t stats of two sample t test
t_p = pd.merge(tstats, pvals)

## sort and reset index
t_p.sort(['ym'], inplace=True)
t_p.reset_index(inplace=True, drop=True)


## graph
fig1 = plt.figure() # intialize a figure
ax1 = fig1.add_subplot(2,1,1)   # create a 2x1 (RxC) matrix, first panel to ax1
ax1.plot(t_p['tstat'])  # plot data (x axis is index)
ax1.axhline(2, color='r', linestyle='--') # add horizontal lines with .axhline (vertical with .axvline)
ax1.axvline(6, color='g', linestyle='--')
ax1.set_title('t-stats over-time (monthly)') # set title
ax2 = fig1.add_subplot(2,1,2)  # second panel to ax2
ax2.plot(t_p['pval'])
ax2.axhline(0.05, color='r', linestyle='--')
ax2.set_title('p-values over-time (monthly)')
ax2.axvline(6, color='g', linestyle='--')



# DAILY AGGREGATION -------------------
grp = df.groupby(['date', 'ID', 'assignment'], as_index=False) # aggregate over date, ID, and keep assignments
agg = grp['kwh'].sum()

# reset the index (multilevel at the moment)
agg = agg.reset_index() # drop the multi-index
grp = agg.groupby(['date', 'assignment'])

## split up treatment/control
trt = {k[0]: agg.kwh[v].values for k, v in grp.groups.iteritems() if k[1] == 1} # get set of all treatments by date
ctrl = {k[0]: agg.kwh[v].values for k, v in grp.groups.iteritems() if k[1] == 0} # get set of all controls by date
keys = ctrl.keys()

## better yet, make dfs!
tstats = DataFrame([(k, np.abs(float(ttest_ind(trt[k], ctrl[k], equal_var=False)[0]))) for k in keys],
    columns = ['date', 'tstat']) # get t stats of two sample t test
pvals = DataFrame([(k, ttest_ind(trt[k], ctrl[k])[1]) for k in keys],
    columns = ['date', 'pval']) # get t stats of two sample t test
t_p = pd.merge(tstats, pvals)

## sort and reset index
t_p.sort(['date'], inplace=True)
t_p.reset_index(inplace=True, drop=True)


## graph
fig2 = plt.figure() # intialize a figure
ax3 = fig2.add_subplot(2,1,1)   # create a 2x1 (RxC) matrix, first panel to ax3
ax3.plot(t_p['tstat'])  # plot data (x axis is index)
ax3.axhline(2, color='r', linestyle='--') # add horizontal lines with .axhline (vertical with .axvline)
ax3.axvline(171, color='g', linestyle='--')
ax3.set_title('t-stats over-time (daily)') # set title
ax4 = fig2.add_subplot(2,1,2)  # second panel to ax4
ax4.plot(t_p['pval'])
ax4.axhline(0.05, color='r', linestyle='--')
ax4.set_title('p-values over-time (daily)')
ax4.axvline(171, color='g', linestyle='--')
plt.show()