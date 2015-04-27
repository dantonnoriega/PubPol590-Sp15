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

main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"
root = main_dir + "data/"


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

# EXPORT ------------------
df_ts.to_csv(root + "timeseries_correction.csv", index=False)
