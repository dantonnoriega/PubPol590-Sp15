from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/dnoriega/Dropbox/pubpol590_sp15/data_sets/"
git_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/03_data_cleaning/"
csv_file_good = "L3/sample_data_unclean.csv"
csv_file_bad = "/L3/sample_data_unclean.csv" # only ABSOLUTE paths start with / or \


# OS MODULE ------------------------

df = pd.read_csv(os.path.join(main_dir, csv_file_good)) # ERROR
df = pd.read_csv(os.path.join(main_dir, csv_file_bad)) # yay
# more reliable than `+`

# PYTHON DATA TYPES ------------------------------

## strings
str1 = "hello, computer"
str2 = 'hello, human'
str3 = u'eep'

type(str1)
type(str2)
type(str3)
[type(x) for x in [str1, str2, str3]]

## numeric
int1 = 10
float1 = 20.56
long1 = 20000022021928847010923280892829210982
[type(x) for x in [int1, float1, long1]]

## logical
bool1 = True
notbool1 = 0
bool2 = bool(0)
[type(x) for x in [bool1, notbool1, bool2]]


# CREATING LISTS and TUPLES ----------------------------

## in brief, you can change list elements, not tuples
## Series and DataFrame values are like list elements, you can change them

## list are made using []
list1 = [] # empty list
list1
list1 = [1, 2, 3]
list1
list1[2] = 5
list1
type(list1)

## tuples are made using ()
tup1 = (1, 2, 3)
tup1
tup1[2] = 5 # error
type(tup1)

## can convert either using list() or tuple()
list2 = list(tup1)
tup2 = tuple(list1)
list2
tup2

## we can append entire objects or extend a current object with more values
## we will be using lists because we want to change things!
list2.append([7,8]) # adds the ENTIRE list object
list2
list2.extend([9,10,11]) # extends the current list with the ELEMENTS of the added list
list2

## can check length using `len` function
len(list1)
len(list2)
list2.extend([20])
len(list2)

# CONVERTING LISTS TO SERIES AND DATAFRAMES -------------------

## Converting list to Serie and multiple lists to DataFrame
list3 = range(5,10) # range(n,m) -- quick way to make a list from n to m-1
list3
list4 = range(5) # range(m) -- defaults to 0 to m-1
list4

## create Serie
# easy to make list into series
s1 = Series(list3)
s1
s2 = Series(list4)
s2

## create DataFrame from lists OR series
# LISTS MUST BE SAME LENGTH
zip(list2, list3, list4) # creates element wise combos of lists
df1 = DataFrame(zip(list3, list4), columns = ['A', 'B'])
df1

zip(s1, s2) # creates element wise combos of lists
df1 = DataFrame(zip(s1, s2), columns = ['A', 'B'])
df1

# using dict notation, {} with keys in quotes ' ' followed by : and then the list
df2 = DataFrame({'A' : list3, 'B' : list4})
df2

df2 = DataFrame({'A' : s1, 'B' : s2})
df2

## create DataFrame from Series ONLY
# using pd.concat
df3 = pd.concat([list3, list4]) # fail
df3 = pd.concat([s1, s2]) # yay


# FOR LOOPS


for v in df['consump']:
    type(v)

for i, v in df.iteritems(): # gets values directly
    print(v)








