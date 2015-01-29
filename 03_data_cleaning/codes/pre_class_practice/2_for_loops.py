from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/dnoriega/Dropbox/pubpol590_sp15/data_sets/"
git_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/03_data_cleaning/"
csv_file = "L3/sample_data_unclean.csv"

# FOR LOOPS -----------------------------

df = pd.read_csv(os.path.join(main_dir, csv_file))
list1 = range(0,5)
list2 = ['a', 'b', 'c']
list3 = [1, 'a', True]


## essential to iterate over objects.
# things are evaluated in the for loop. to see them, use `print`
for v in list1:
    v

## need to use print
for v in list1:
    print(v)

for v in list3:
    print(v, type(v))

## making a new list
list4 = [] # empty list
list4

for v in list1:
    list4.extend([v])

list4

## can be reduced to one line but MUST use [] around
## needs to result in an object. for loops are not objects
v for v in list1 # error
[v for v in list1]
list5 = [type(v) for v in list3]
list5

# we can also use for loops over enumerate()
[[i, v] for i, v in enumerate(list3)] # i gives the iteration, v is the value
list6 = [[i, v] for i, v in enumerate(list3)]

# USING FOR LOOPS WITH DATAFRAMES AND SERIES ---------------------------

## series
[v for v in df['consump']]
[type(v) for v in df['consump']]
[[i, v] for i, v in enumerate(df['consump'])]


for v in df['consump']:
    type(v)

for i, v in df.iteritems(): # gets values directly
    print(v)



