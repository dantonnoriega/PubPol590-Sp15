
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
        logit_results = do_logit(df_pretrial, i, j, add_D=None, mc = False)


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



