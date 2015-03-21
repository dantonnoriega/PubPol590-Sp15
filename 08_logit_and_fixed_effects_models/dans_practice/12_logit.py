# logit (dan's practice)## gen data
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm
import os

main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"
root = main_dir + "/data/"
paths = [root + v for v in os.listdir(root) if v.startswith("08_")]

# IMPORT AND ADD/DROP VARIABLES ---------------------------
## np.datetime64 is MUCH faster but can't handle timezones. need to adjust that by hand.
df = pd.read_csv(paths[1], header=0, parse_dates=[1], date_parser=np.datetime64)
df_assign = pd.read_csv(paths[0], header=0) # will use later

df['year'] = df['date'].apply(lambda x: x.year)
df['month'] = df['date'].apply(lambda x: x.month)

# MONTHLY AGGREGATION --------------------
grp = df.groupby(['year', 'month', 'panid'])
df = grp['kwh'].sum().reset_index()

# PIVOT THE DATA -------------------------

df['mo_str'] = ['0' + str(v) if v < 10 else str(v) for v in df['month']] # add '0' to < 10
df['kwh_ym'] = 'kwh_' + df.year.apply(str) + '_' + df.mo_str.apply(str)

# pivot on the new column name
df_piv = df.pivot('panid', 'kwh_ym', 'kwh')

# the panids become the index. lets reset it.
df_piv.reset_index(inplace=True)
df_piv.columns.name = None # remove the label of columns (confusing)

## MERGE OTHER DATA TO PIVOTED DATA ------------------------
df = pd.merge(df_assign, df_piv) # want the other info to be first in column order
del df_piv, df_assign

## GENERATE DUMMIES VARIABLES --------
## by default, will make dummy vectors for ALL "object" or "category" types
df1 = pd.get_dummies(df, columns = 'gender')
df1.drop(['gender_M'], axis = 1, inplace = True)

## SET UP DATA ---------------------
# get kwh_cols that we care about
kwh_cols = [v for v in df1.columns.values if v.startswith('kwh')]
kwh_cols = [v for v in kwh_cols if int(v[-2:]) < 3] # baller code. i'll explain in class.

## add additional cols
cols = ['gender_F'] + kwh_cols

# set up y and X
y = df1['assignment']
X = df1[cols] # extend list of kwh names
X = sm.add_constant(X)

## RUN LOGIT
logit_model = sm.Logit(y, X) # linearly prob model
logit_results = logit_model.fit() # get the fitted values
print(logit_results.summary()) # print pretty results (no results given lack of obs)

