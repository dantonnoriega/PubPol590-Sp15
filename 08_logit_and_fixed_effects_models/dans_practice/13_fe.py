# FIXED EFFECTS (dan's practice)
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm
import os


main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"
root = main_dir + "/data/"
paths = [root + v for v in os.listdir(root) if v.startswith("08_")]

"""NOTE: USING NOTATION FROM ALLCOTT 2010"""


# IMPORT ---------------------------
## np.datetime64 is MUCH faster but can't handle timezones. need to adjust that by hand.
df = pd.read_csv(paths[1], header=0, parse_dates=[1], date_parser=np.datetime64)
df_assign = pd.read_csv(paths[0], header=0) # will use later
df_assign.rename(columns={'assignment':'T'}, inplace=True) # rename 'assignment' to 'T'

# ADD/DROP VARIABLES ---------------------------
## create a 'ym' object that will convert correctly as type `datetime64`
ym = pd.DatetimeIndex(df.date).to_period('M') # 'M' = month, 'D' = day. check documentation for more.
df['ym'] = ym.values

# MONTHLY AGGREGATION --------------------
grp = df.groupby(['ym','panid'])
df = grp['kwh'].sum().reset_index()

# MERGE AND RESET INDEX --------------
df = pd.merge(df, df_assign)
df.reset_index(drop=True, inplace=True)


# RUN FE MODEL (DEMEANING WITH `demean` function) -----------------

## SET UP DATA
from fe_functions import demean # demean.py must be within the same folder as your code

df['log_kwh'] = df['kwh'].apply(np.log)
cols = ['log_kwh', 'TP', 'P']
panid = 'panid'
df_dm = demean(df, cols, 'panid')

## SET VARIABLES
## for y and X, we use the de-meaned values. we do NOT de-mean the dummy variables.

mu = pd.get_dummies(df['ym'], prefix = "ym").iloc[:, 1:-1] # get time control dummies from `df`
y = df_dm['log_kwh'] # demean values from `df_dm`
X = df_dm[['TP', 'P']]

fe_model = sm.OLS(y_dm, pd.concat([X_dm, mu], axis=1)) # linearly prob model
fe_results = fe_model.fit() # get the fitted values
print(fe_results.summary()) # print pretty results (no results given lack of obs)



## RUN FE MODEL (DUMMIES) ----------------

# SET UP DATA
## when using pd.get_dummies on a SERIES, it is prudent to create a prefix using option `prefix = "text"`
## keep all but the last column using .iloc[:, :-1]
mu = pd.get_dummies(df['ym'], prefix = "ym").iloc[:, 1:-1]
v = pd.get_dummies(df['panid'], prefix = "panid").iloc[:, :-1]
df['P'] = 0 + (df['ym'] > 541) # post treatment indicator
df['TP'] = df['T']*df['P']

# set up y and X
y = df['kwh'].apply(np.log)
X = pd.concat([df[['TP', 'P']], mu, v], axis=1)
X = sm.add_constant(X)

fe_model = sm.OLS(y, X) # linearly prob model
fe_results = fe_model.fit() # get the fitted values
cl_se = se_cluster(fe_results, 'panid')
print(fe_results.summary()) # print pretty results (no results given lack of obs)


## RUN FE MODEL (DEMEANING WITH MATRICES) -----------------
# SET UP DATA ---------------------
df['log_kwh'] = df['kwh'].apply(np.log)
i = np.mat(pd.get_dummies(df['panid'], prefix = "panid").values) # get dummy matrix by ids
T = len(np.unique(df['ym'])) # get length of time
y = np.mat(df['log_kwh'].values).getT() # get vector for y
X_vars = ['TP', 'P'] # set X variables to extract
X = np.mat(df[X_vars].values) # get X matrix

## demean y and X
y_dm = DataFrame(y - (1/T)*np.dot(i, np.dot(i.getT(), y)), columns = ['log_kwh'])
X_dm = DataFrame(X - (1/T)*np.dot(i, np.dot(i.getT(), X)), columns = X_vars)
X_dm = sm.add_constant(X_dm)
mu = pd.get_dummies(df['ym'], prefix = "ym").iloc[:, 1:-1]

fe_model = sm.OLS(y_dm, pd.concat([X_dm, mu], axis=1)) # linearly prob model
fe_results = fe_model.fit() # get the fitted values
cl_se = se_cluster(fe_results, 'panid')
print(fe_results.summary()) # print pretty results (no results given lack of obs)




