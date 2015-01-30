from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/dnoriega/Desktop/pubpol590_data"
git_dir = "/Users/dnoriega/Desktop/pubpol590"
csv_file = "sample_missing.csv"

# IMPORTING DATA: SETTING MISSING VALUES --------------------

df = pd.read_csv(os.path.join(main_dir, csv_file))
df.head() # see top 5 values by default. notice first 5 are periods '.'
df.head(10) # see top n values for `head(n)`
df[0:10] # same as above
df.tail(10) # see bottom n values for `tail(n)`
df['consump'].head(10).apply(type) # apply the type() function to rows 0 to 9 of consump

## we DONT want string data. periods '.' are common placeholders for missing data
## use option `na_values` to set the missing value sentinels
missing = ['.', 'NA', 'NULL', '']
df = pd.read_csv(os.path.join(main_dir, csv_file), na_values = missing)
df.head(10)
df['consump'].head(10).apply(type) # apply the type() function to rows 0 to 9 of consump



# MISSING DATA (USING SMALLER DATA SET) ----------------------------------------

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
zip1 = zip([2, 4, 8],
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
df2

## we can also drop columns or rows with missing values using `dropna`
## `dropna` also has two options:
##  - `axis` where `axis = 0` is rows and = 1 is columns
##  - `how` where ` how = 'any' ` means drop if row/col has ANY missing values
##          and ` how = 'all' ` means drop if row/col has ALL missing values
##  for more, type 'DataFrame.dropna?' in the console
df1.dropna() # default is drop ROWS with ANY missing values
df1.dropna(axis = 0, how = 'any') # drop ROWS with ANY missing values
df1.dropna(axis = 1, how = 'any') # drop cols with ANY missing values
df1.dropna(axis = 0, how = 'all') # drop ROWS with ALL missing values
                                  # (nothing happens since no row/col are totally empty)

# SEEING ROWS WITH MISSING DATA ----------------------

## we want to search a column of a DataFrame for missing values then extract
##      those rows from the data set to isolate them
df1['c'].isnull() # return boolean vector
rows = df1['c'].isnull()
df1[rows] # extract rows where column 'c' has missing values






