## group task practice
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import pytz
from datetime import datetime, timedelta

# main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"
# root = main_dir + "06_plotting/data/"

# TIMESERIES CORRECTION -----------------------------------

def gen_kwh_data(start_datetime, end_datetime, delta, ids):

    # send in list of IDs where each ID is repeated and stacked `n` times
    def stack_ids(ids, n):
        y = [[x]*n for x in ids]
        return sum(y, [])

    # fill in an empty list with the DST corrected dates
    d = start_datetime
    ts = [d]

    while d < end_datetime:
        d = tz.normalize(d + delta)  # Add 30 minutes
        ts.append(d)


    stacked_ids = stack_ids(ids, len(ts))

    kwh = 5*np.random.beta(2, 4, len(stacked_ids))

    # combine everything into a dataframe
    df = DataFrame({ 'panid' : stacked_ids,
                        'date' : list(ts)*len(ids),
                        'kwh' : kwh
                    })

    # arrange column order
    df = df[[2,0,1]]

    return df


ids = [1, 2, 3, 4, 5] # id vector
tz = pytz.timezone('US/Eastern') # this is the timezone smart meters are in
delta = timedelta(minutes=30)
start_datetime = tz.localize(datetime(2015, 1, 1, 0, 0, 0)) # start date of experiment
end_datetime = tz.localize(datetime(2015, 2, 1, 0, 0, 0) - delta) # end date of experiment

np.random.seed(1789)
df = gen_kwh_data(start_datetime, end_datetime, delta, ids)

# export a csv copy without index
df.to_csv("/Users/dnoriega/Desktop/30min_samples.csv", index = 0)