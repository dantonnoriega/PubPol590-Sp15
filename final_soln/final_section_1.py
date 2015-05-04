## practice for final
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os


#####################################################################
#                    SECTION 1 -- PYTHON                            #
#####################################################################

## PART A -- IMPORT AND CLEAN CONSUMPTION DATA
main_dir = "/Users/dnoriega/Dropbox/PubPol590_Sp15/"
root = main_dir + "pubpol590_final/section_1/"

# ADVANCED PATHING ------------------------------------
paths = [os.path.join(root, v) for v in os.listdir(root) if v.startswith("gas_")]

# IMPORT DATA ------------------------------------
df = pd.concat([pd.read_csv(v) for v in paths])

# CLEAN ERRORS ------------------------
## drop duplicated values with same ID and date (ignore consumption)
df = df.drop_duplicates(['ID', 'date_cer'])

## replace -999 and np.nan with zeros
df.kwh[(df.kwh < 0)] = 0
df.kwh[df.kwh.isnull()] = 0 # HINT: use df.kwh.isnull() or np.nan(df.kwh) to get boolean vector of missing values
print "\n\n\n" # creates space between prints
print df.shape
print df.kwh.mean()



# PART B -- IMPORT AND MERGE ALLOCATION AND TIME DATA
df_alloc = pd.read_csv(root + "residential_allocations.csv", usecols=[0,1])
df_time = pd.read_csv(root + "time_correction.csv", parse_dates=[0])

# NEW VARS ---------------------
df['hour_cer'] = df['date_cer'] % 100
df['day_cer'] = (df['date_cer'] - df['hour_cer']) / 100

# STACK AND MERGE --------------------
df = pd.merge(df, df_alloc)
df = pd.merge(df, df_time)

print "\n\n\n" # creates space between prints
print df[df.ID == 1021].head(20)



# PART C -- PIVOT MONTHLY AGGREGATE DATA
# AGGREGATE MONTHLY CONSUMPTION
grp = df.groupby(['ID', 'allocation', 'year', 'month', 'ym'])
df_agg = grp['kwh'].sum().reset_index() # HINT: reset index to get back a dataframe
df_agg['mo_str'] = ['0' + str(v) if v < 10 else str(v) for v in df_agg['month']] # add '0' to < 10
df_agg['kwh_ym'] = 'kwh_' + df_agg.year.apply(str) + '_' + df_agg.mo_str.apply(str)

# pivot on the new column name
df_piv = df_agg.pivot('ID', 'kwh_ym', 'kwh')

# the panids become the index. lets reset it.
df_piv.reset_index(inplace=True)
df_piv.columns.name = None # remove the label of columns (confusing)

## merge other data to pivoted data
df_piv = pd.merge(df_alloc, df_piv) # want the other info to be first in column order
print "\n\n\n"
print df_piv.shape
print df_piv.head()



## PART D -- PLOT AVERAGE MONTHLY CONSUMPTION
# average monthy consumption by treatment
df_kwh_avg = df_agg.groupby(['allocation', 'ym'])['kwh'].mean() # hint, use variable 'ym'
print df_kwh_avg

# plot
df_kwh_avg.unstack().transpose().plot()

