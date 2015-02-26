## dan's practice (regression)
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm # we use statsmodel (sm) for stats and econometrics

main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"

# ADVANCED PATHING ------------------------------------
root = main_dir + "/data/"

# IMPORT DATA ------------------------------------
df = pd.read_csv(root + "07_kwh_wide.csv", header=0)

# SIMPLE LINEAR PROBABILITY MODEL ------------------
## lets see if consumption before a certain date determined your assignment

df['T'] = 0 + (df['assignment'] == 'T') # need assignments in 0, 1 format

## SET UP DATA
# get kwh_cols that we care about
kwh_cols = [v for v in df.columns.values if v.startswith('kwh')]
kwh_cols = [v for v in kwh_cols if int(v[-2:]) < 4] # baller code. i'll explain in class.

# set up y and X
y = df['T']
X = df[kwh_cols]
X = sm.add_constant(X)

## RUN OLS (LINEAR PROBABILITY MODEL)
## great source:
##  http://statsmodels.sourceforge.net/devel/examples/notebooks/generated/ols.html
ols_model = sm.OLS(y, X) # linearly prob model
ols_results = ols_model.fit() # get the fitted values
print(ols_results.summary()) # print pretty results (no results given lack of obs)

