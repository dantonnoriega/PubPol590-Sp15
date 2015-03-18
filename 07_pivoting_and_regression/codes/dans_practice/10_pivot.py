## dan's practice (pivoting)
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from dateutil import parser # use this to ensure dates are parsed correctly


main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"

# ADVANCED PATHING ------------------------------------
root = main_dir + "/data/"

# IMPORT DATA ------------------------------------
df = pd.read_csv(root + "sample_30min.csv", header=0, parse_dates=[1],
    date_parser=parser.parse)
df_assign = pd.read_csv(root + "sample_assignments.csv", usecols = [0,1])


# MERGE ---------
df = pd.merge(df, df_assign)

# ADD/DROP VARIABLES ---------------------------
df['year'] = df['date'].apply(lambda x: x.year)
df['month'] = df['date'].apply(lambda x: x.month)
df['day'] = df['date'].apply(lambda x: x.day) # x.day returns integer; x.date() returns date object
df['ymd'] = df['date'].apply(lambda x: x.date()) # notice the parentheses in `.date()`


# Daily AGGREGATION --------------------

grp = df.groupby(['year', 'month', 'day', 'panid', 'assignment'])
df1a = grp['kwh'].sum().reset_index()

grp = df.groupby(['ymd', 'panid', 'assignment'])
df1b = grp['kwh'].sum().reset_index()

# PIVOT THE DATA -------------------------

## data is currently in "long" format. want the data to be in "wide" format.
## aka 'long' to 'wide'

## 1. we need to create our column names
# create string names that denote consumption and date
# use ternery expression: [true-expr(x) if condition else false-expr(x) for x in list]
df1a['day_str'] = ['0' + str(v) if v < 10 else str(v) for v in df1a['day']] # add '0' to < 10
df1a['kwh_ymd'] = 'kwh_' + df1a.year.apply(str) + '_' + df1a.month.apply(str) + '_' + df1a.day_str.apply(str)

# if you use 'ymd', you can skip this string play
df1b['kwh_ymd'] = 'kwh_' + df1b.ymd.apply(str)

# pivot on the new column name
df1_piv = df1b.pivot('panid', 'kwh_ymd', 'kwh')

# the panids become the index. lets reset it.
df1_piv.reset_index(inplace=True)
df1_piv
df1_piv.columns.name = None # remove the label of columns (confusing)
df1_piv

## MERGE OTHER DATA TO PIVOTED DATA ------------------------
df2 = pd.merge(df_assign, df1_piv) # want the other info to be first in column order


## EXPORT DATA ---------------------
df2.to_csv(root + "07_kwh_wide.csv", sep = ",", index=False)



