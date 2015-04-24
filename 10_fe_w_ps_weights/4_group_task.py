
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm
import os

git_dir = '/Users/dnoriega/GitHub/Duke_PUBPOL590/'
root = '10_fe_w_ps_weights/dans_practice/'
data_dir = '/Users/dnoriega/Dropbox/pubpol590_sp15/data_sets/CER/tasks/4_task_data/'

# CHANGE WORKING DIRECTORY -----------------
os.chdir(git_dir + root) # change working directory (wd)
from logit_functions import * # if `do_logit.py` is in wd, then it will import!

# IMPORT DATA ------------
nas = ['', ' ', 'NA'] # set NA values so that we dont end up with numbers and text
df = pd.read_csv(data_dir + 'task_4_kwh_w_dummies_wide.csv', na_values = nas)


######################################
#       SECTION 1
######################################

# GET TARIFFS --------------
tariffs = [v for v in pd.unique(df['tariff']) if v != 'E']
stimuli = [v for v in pd.unique(df['stimulus']) if v != 'E']
tariffs.sort() # make sure the order correct with .sort()
stimuli.sort()

# RUN LOGIT -----------------
# set option `D = None` if you want the logit to find dummy variables automatically
#   (assumes dummies variable start with "D_" and consump variables with "kwh_")
# option `mc` is whether or not to remove highly multicollinear values

# REMEMBER, keep only PRE-TRIAL consumption data. Dummies are already from pretrial.

drop = [v for v in df.columns if v.startswith("kwh_2010")] # find columns to drop
df_pretrial = df.drop(drop, axis=1)

for i in tariffs:
    for j in stimuli:
        # save the results of the function!
        logit_results, df_logit = do_logit(df_pretrial, i, j, add_D=None, mc = False)


# QUICK MEANS COMPARISON WITH T-TEST BY HAND --------------------
# create means
df_mean = df_pretrial.groupby('tariff').mean().transpose()

# do a t-test "by hand"
df_s = df_pretrial.groupby('tariff').std().transpose() # the index becomes variable names
df_n = df_pretrial.groupby('tariff').count().transpose().mean()
tstat_top = df_mean['C'] - df_mean['E']
tstat_bottom = np.sqrt(df_s['C']**2/df_n['C'] + df_s['E']**2/df_n['E'])
tstat = tstat_top/tstat_bottom
sig = tstat[np.abs(tstat) > 2]
sig.name = 't-stats' # sig is a series. you can name a Series easily this way
print "\n\n\n", sig

######################################
#       SECTION 2
######################################

## get the predicted values ("p-hats") from the logit model used for the imbalance check.
## assign them to the saved dataframe
df_logit['p_hat'] = logit_results.predict()
df_logit['trt'] = 0 + (df_logit['tariff'] == 'C')
df_logit['w'] = np.sqrt(df_logit.trt/df_logit.p_hat + (1 - df_logit.trt)/(1 - df_logit.p_hat))
df_w = df_logit[['ID', 'trt', 'w']]

######################################
#       SECTION 3
######################################

## FIXED EFFECTS WITH DEMEAN FUNCTIONS --------------

df = pd.read_csv(data_dir + 'task_4_kwh_long.csv', na_values = nas)
df = pd.merge(df, df_w)

# set up variables
# create 'ym' variable
df['trt_trial'] = df['trt']*df['trial']
df['log_kwh'] = (df['kwh'] + 1).apply(np.log)
# df.to_csv("/Users/dnoriega/Desktop/test2.csv", index=False)
df['mo_str'] = np.array(["0" + str(v) if v < 10 else str(v) for v in df['month']])
df['ym'] = df['year'].apply(str) + "_" + df['mo_str']

## SET VARIABLES
## for y and X, we use the de-meaned values. we do NOT de-mean the dummy variables.
mu = pd.get_dummies(df['ym'], prefix = "ym").iloc[:, 1:-1] # get time control dummies from `df`
w = df['w']
y = df['log_kwh'] # demean values from `df_dm`
P = df[['trial']]
TP = df['trt_trial']
X = pd.concat([TP, P, mu], axis=1)

# DEMEAN
from fe_functions import *
ids = df['ID']
y = demean(y, ids)
X = demean(X, ids)
# pd.concat([y, X, w], axis=1).to_csv("/Users/dnoriega/Desktop/test3.csv", index=False)

## WITHOUT WEIGHTS
fe_model = sm.OLS(y, X) # linearly prob model
fe_results = fe_model.fit() # get the fitted values
print(fe_results.summary()) # print pretty results (no results given lack of obs)

# WITH WEIGHTS
## apply weights to data
y = y*w # weight each y
nms = X.columns.values # save column names
X = np.array([x*w for k, x in X.iteritems()]) # weight each X value
X = X.T # transpose (necessary as arrays create "row" vectors, not column)
X = DataFrame(X, columns = nms) # update to dataframe; use original names

fe_w_model = sm.OLS(y, X) # linearly prob model
fe_w_results = fe_w_model.fit() # get the fitted values
print(fe_w_results.summary()) # print pretty results (no results given lack of obs)


