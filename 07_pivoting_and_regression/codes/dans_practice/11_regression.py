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
df = pd.read_csv(root + "kwh_wide.csv", header=0)

