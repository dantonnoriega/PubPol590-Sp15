from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from dateutil import parser # use this to ensure dates are parsed correctly

main_dir = "/Users/dnoriega/GitHub/Duke_PubPol590/"
root = main_dir + "/data/"

# import data --------------
df = pd.read_csv(root + "sample_30min.csv", header=0, parse_dates=[1],
            date_parser=parser.parse)
df_assign = pd.read_csv(root + "sample_assignments.csv", usecols = [0,1])

# merge -----
df = pd.merge(df, df_assign)

# add/drop variables ------
df['year'] = df['date'].apply(lambda x: x.year)
df['month'] = df['date'].apply(lambda x: x.month)
df['day'] = df['date'].apply(lambda x: x.day)
df['ymd'] = df['date'].apply(lambda x: x.date())


# daily aggregation
grp = df.groupby(['year', 'month', 'day', 'panid', 'assignment'])
grp = df.groupby(['ymd', 'panid', 'assignment'])
df1 = grp['kwh'].sum().reset_index()

# PIVOT DATA ---------------
# go from 'long' to 'wide'

## 1. create column names for wide data
# create strings names and denote consumption and date
# use ternery expression: [true-expr(x) if condition else false-exp(x) for x in list]
#df1['day_str'] = ['0' + str(v) if v < 10 else str(v) for v in df1['date']] # add '0' to < 10
#df1['kwh_ymd'] = 'kwh_' + df1.year.apply(str) + '_' + df1.month.apply(str) + 
#            '_' + df1.day_str.apply(str)

df1['kwh_ymd'] = 'kwh_' + df1['ymd'].apply(str)

# 2. pivot! aka long to wide
df1_piv = df1.pivot('panid', 'kwh_ymd', 'kwh')

# clean up for making things pretty
df1_piv.reset_index(inplace=True) # this makes panid its own variable
df1_piv
df1_piv.columns.name = None
df1_piv

# MERGE TIME invariant data ----
df2 = pd.merge(df_assign, df1_piv) # this attachin order looks better

## export data data for regression
df2.to_csv(root + "07_kwh_wide.csv", sep = ",", index=False)