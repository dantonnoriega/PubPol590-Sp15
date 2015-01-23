from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# SET UP FILES -----------------------------------------------------------------------
## create a main directory link and a subpath to file
## NOTE: anything in quotes `" "` is a data type called a 'string'. You should
## ALWAYS make file paths into strings to avoid parsing errors.
main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/"
csv_file = "02_data_structures_and_importing_data/data/sample_data_clean.csv"
txt_file = "02_data_structures_and_importing_data/data/sample_data_clean.txt"
xls_file = "02_data_structures_and_importing_data/data/sample_data_clean.xls"

## we can join strings together (aka 'concatenate') using the plus `+` sign
main_dir + csv_file

# IMPORT DATA ------------------------------------------------------------------------
## We can import most raw data using the following functions:
#       pd.read_csv()   --  read .csv values
#       pd.read_txt()   --  read any 'table' like data, like tab-delimited .txt files
#       pd.read_excel() --  read .xls files

## create a dataframe, df, by importing data using pandas
pd.read_csv(main_dir + csv_file)

## we can assign any object to a variable using the equals sign `=`
df = pd.read_csv(main_dir + csv_file) # need to use 'pd.' before using any pandas function
df2 = pd.read_table(main_dir + txt_file) # default is tab-delimiter, or sep = "\t"
df3 = pd.read_excel(main_dir + xls_file)

## we can do 'boolean comparison' using logical statements: `>`, `<`, `==`, `>=`, `<=`, `!=`
df == df2
df == df3

# EXPLORING THE DATA ------------------------------------------------------------------
type(df) # check the object type! notice that it is a DataFrame
list(df) # this will tell you the column names! (if there are any)

## can extract data columns in two ways
df.consump # internal attribute notation using a dot '.'
df['consump'] # using 'dictionary-like' or 'dict' key notation

## we can assign columns (Series) since they are also objects
c = df.consump
c2 = df['consump']

c == c2 # shows that they are equal. notice that '==' is a logical test
type(c) # notice that its a Series!


# ROW SLICING AND BOOLEAN INDEXING ------------------------------------------------------
## we can extract rows of data using slicing or 'boolean' indexing
## slicing -- using `:` in a data frame
#df[2] # fails. cant just write one line
df[:5] # first row (0) until the 4th row (5 - 1 = 4)
df[0:5] # same as above
df[5:10] # df[m:n] -- extract rows m to n-1

## we can get rows from a column (Series) in a DataFrame by slicing as well
df.consump[:5] # df.consump moves into the column then you use the same [m:n] notation
df['consump'][:5] # works with 'dict' keys too
c[5:10] # if you assigned the series, you can just use [m:n] slicing

## what if we want only the rows of data for the 4th participant (panid == 4)?
##  we can use boolean indexing!

df.panid == 4 # find where `panid` equals 4. we use the boolean test for equality, `==`
df[df.panid == 4] # we can then use that boolean index vector to extract only the rows we want

## how would you extract the data for everyone BUT person 4?
df[df.panid < 4]
df[df.panid != 4]

