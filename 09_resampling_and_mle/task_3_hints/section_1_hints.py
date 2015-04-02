from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

main_dir = "/Users/dnoriega/Dropbox/PubPol590_Sp15/"
root = main_dir + "data_sets/CER/tasks/3_task_data/"

df = pd.read_csv(root + "allocation_subsamp.csv")

# Extract Only Control using Boolean Indexing
# equals ==; greater than >; less than <; not equals !=; greater equal >= etc.
indx = df['tariff'] == 'E'
df[indx]

# Extract Control or Treatment A1
indx1 = (df['tariff'] == 'A') 
df[indx1]
## logical 'and' = & ; 'or' = |
indx2 = ((df['tariff'] == 'A') & (df['stimulus'] == '1')) 
df[indx2]
indx3 = ((df['tariff'] == 'A') & (df['stimulus'] == '1')) | (df['tariff'] == 'E')
df[indx3]
df[indx | indx2]

# SHORTCUT
df['tarstim'] = df['tariff'] + df['stimulus']
## find B3 or EE
indx4 = (df['tarstim']=='EE') | (df['tarstim']=='B3')
df[indx4]

# Example of 'hardcoding'
dfEE = df[df['tarstim']=='EE']
dfA1 = df[df['tarstim']=='A1']
dfA3 = df[df['tarstim']=='A3']
dfB1 = df[df['tarstim']=='B1']
dfB3 = df[df['tarstim']=='B3']

np.random.seed(1789)
sampEE = np.random.choice(dfEE['ID'], 300, replace = False)
sampA1 = np.random.choice(dfA1['ID'], 150, replace = False)
sampA3 = np.random.choice(dfA3['ID'], 150, replace = False)
sampB1 = np.random.choice(dfB1['ID'], 50, replace = False)
sampB3 = np.random.choice(dfB3['ID'], 50, replace = False)


ids = sampEE.tolist() + sampA1.tolist() + sampA3.tolist()
DataFrame(ids, columns = ['ID'])

## example logit
dfEEA1 = pd.concat([dfEE, dfA1], axis = 0)
dfEEA1['T'] = 0 + (dfEEA1['tarstim'] != 'EE')



