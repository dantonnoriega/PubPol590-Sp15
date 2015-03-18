from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm

main_dir = "/Users/dnoriega/GitHub/Duke_PubPol590/"
root = main_dir + "/data/"

# IMPORT DATA -----------
df = pd.read_csv(root + "07_kwh_wide.csv", header=0)

# SIMPLE LINEAR PROBABLY MODEL (LPM) -------------
## lets see if consumption before a certain date determined your assignment
df['T'] = 0 + (df['assignment'] == 'T')

## SET UP DATA ---------
# get X matrix (left hand variables for our regression)
kwh_cols = [v for v in df.columns.values if v.startswith('kwh')]

# pretend that the treatment occurred in 2015-01-04. we want dates before.
kwh_cols = [v for v in kwh_cols if int(v[-2:]) < 4]

# set up y and X
y = df['T']
X = df[kwh_cols]
X = sm.add_constant(X)

# RUN OLS -----------
ols_model = sm.OLS(y, X) # lpm
ols_results = ols_model.fit() # fit the model
print(ols_results.summary())