## group task 3 practice
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm

main_dir = "/Users/dnoriega/Dropbox/PubPol590_Sp15/"
root = main_dir + "data_sets/CER/tasks/3_task_data/"


#####################################################################
#                           SECTION 1                               #
#####################################################################

df_alloc = pd.read_csv(root + "allocation_subsamp.csv")

## SET SEED AND SAMPLE
np.random.seed(1789)

ids = df_alloc['ID']
tariffs = [v for v in pd.unique(df_alloc['tariff']) if v != 'E']
stimuli = [v for v in pd.unique(df_alloc['stimulus']) if v != 'E']
tariffs.sort() # make sure the order correct with .sort()
stimuli.sort()

EE = np.random.choice(ids[df_alloc['tariff'] == 'E'], 300, False)

for i in tariffs:
    for j in stimuli:
        n = 150 if i == 'A' else 50
        temp = np.random.choice(ids[(df_alloc['tariff'] == i) & (df_alloc['stimulus'] == j)], n, False)
        EE = np.hstack((EE, temp))

ids = DataFrame(EE, columns = ['ID'])
df = pd.merge(ids, pd.read_csv(root + "kwh_redux_pretrial.csv"))

# MONTHLY AGGREGATION --------------------
grp = df.groupby(['year', 'month', 'ID'])
df = grp['kwh'].sum().reset_index()


# PIVOT THE DATA -------------------------

df['mo_str'] = ['0' + str(v) if v < 10 else str(v) for v in df['month']] # add '0' to < 10
df['kwh_ym'] = 'kwh_' + df.year.apply(str) + '_' + df.mo_str.apply(str)

# pivot on the new column name
df_piv = df.pivot('ID', 'kwh_ym', 'kwh')

# the IDs become the index. lets reset it.
df_piv.reset_index(inplace=True)
df_piv.columns.name = None # remove the label of columns (confusing)

## MERGE OTHER DATA TO PIVOTED DATA ------------------------
df = pd.merge(df_alloc, df_piv) # want the other info to be first in column order
df.to_csv(root + 'data_section2.csv', index = False)

## SET UP DATA ---------------------
# get kwh_cols that we care about
kwh_cols = [v for v in df.columns.values if v.startswith('kwh')]

# LOGIT LOOPS ------------

for i in tariffs:
    for j in stimuli:
        # set up y and X
        indx = (df.tariff == 'E') | ((df.tariff == i) & (df.stimulus == j))
        df1 = df.ix[indx, :].copy() # `:` denotes ALL columns; use copy to create a NEW frame
        df1['T'] = 0 + (df1['tariff'] != 'E') # stays zero unless NOT of part of control
        # print df1

        y = df1['T']
        X = df1[kwh_cols] # extend list of kwh names
        X = sm.add_constant(X)
        # print y, X

        msg = ("\n\n\n\n-----------------------------------------------------------------\n"
        "LOGIT where Treatment is Tariff = %s, Stimulus = %s"
        "\n-----------------------------------------------------------------\n\n\n") % (i, j)

        ## RUN LOGIT
        logit_model = sm.Logit(y, X) # linearly prob model
        logit_results = logit_model.fit() # get the fitted values
        print msg, logit_results.summary() # print pretty results (no results given lack of obs)
