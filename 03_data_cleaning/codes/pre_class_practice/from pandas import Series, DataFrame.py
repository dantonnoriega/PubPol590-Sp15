from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/dnoriega/Desktop/pubpol590_data"
git_dir = "/Users/dnoriega/Desktop/pubpol590"
csv_file = "sample_data_unclean.csv"

# MISSING DATA ----------------------------------------

## quick trick: you can repeat a list by multiplying with a number
['1','2','3']
['1','2','3']*3 # repeats the list three times!

## two types of missing data, `None` and `np.nan`. Both are read as "NaN"
##      which implies missing data. however, `None` is not numeric while
##      `np.nan` is (float). this distinction is important.
## being numeric, `np.nan` is much faster for computing.
## see more at:
##  http://stackoverflow.com/questions/17534106/what-is-the-difference-between-nan-and-none
None
np.nan
type(None)
type(np.nan)

## create a sample data setdd
zip1 = zip([1, 2, np.nan],
            [np.nan, 5, 7],
            [np.nan, np.nan, 22])

df1 = DataFrame(zip1, columns = ['a', 'b', 'c'])
df1


## finding missing values with pandas DataFrame method`isnull` and numpy `isnan`
## returns boolean values where True/False

# search a whole dataframe
df1.isnull()
np.isnan(df1)

# search specific columns
cols = ['a', 'c'] # create a list of column keys
df1[cols]
df1[cols].isnull()

# also works on a series
df1['b']
df1['b'].isnull()

# pandas also has a negation of `isnull`, `notnull`
df1.isnull()
df1.notnull()
df1.isnull() == df1.notnull() # all false! perfectly opposite

# FILLING IN OR DROPPING MISSING VALUES ----------------------------

## using pandas method `fillna`
df1.fillna(999) # put the value you want to fill missing values with
df2 = df1.fillna(999)
df1 == df2 ## can check which elements are equal










df2 = DataFrame({ 'red' : ['a', 'b', 'c']*2, 'green' : [6, 7, 8]*2})
df1_cols = list(df2)
df2 = df2[ ['red', 'green'] ]

df2['blue'] = Series([':(', ':)']*3, index = df2.index)