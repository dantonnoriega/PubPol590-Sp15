from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# DUPLICATED VALUES -----------------------------------

## create a new data frame
zip3 = zip(['red', 'green', 'blue', 'orange']*4, [5, 10, 20, 40]*3, [':(', ':D', ':D']*4)
df3 = DataFrame(zip3, columns = ['A', 'B', 'C'])
df3

## returns boolean vector of duplicated rows of a whole DataFrame or subset using method `duplicated`
## IMPORTANT: python, by default, searches for duplicated values from top-to-bottom
## and will not mark a row as "duplicated" until it actually finds another instance
df3.duplicated() # defaults using all rows searching top-to-bottom
df3.duplicated(take_last = True) # option `take_last = True` searches bottom-to-top

## SUBSET duplicates
# if we want the duplicated criteria to be of a subset, we can do that too
df3.duplicated(subset = ['A', 'B'])
df3.duplicated(['A', 'B']) # same as before


## HOW to get all values that have a duplicate
t_b = df3.duplicated()
b_t = df3.duplicated(take_last = True)
unique = ~(t_b | b_t) # negate where either is true
unique
unique = ~t_b & ~b_t # same as above
unique

# DROPPING DUPLICATES ----------------------------------

## drop duplicates with `drop_duplicates`. same options
df3.drop_duplicates()
df3.drop_duplicates(take_last = True) # notice that the indeces are different

## another way to do this
t_b = df3.duplicated() # find duplicated values from top to bottom
df3[~t_b] # boolean extract the negation of `t_b` using the not symbol `~` (tilde)
df3.drop_duplicates() == df3[~t_b] # the same!

## can also using subset criteria
df3.drop_duplicates(['A', 'B'])

# WHEN TO USE? ------------------------------

## if you want to keep one duplicated value (from the top) and remove others
df3.drop_duplicates()

## same but from the bottom
df3.drop_duplicates(take_last = True)

## remove ALL values that have a duplicate in the data set (purge all duplicates)
t_b = df3.duplicated()
b_t = df3.duplicated(take_last = True)
unique = ~(t_b | b_t) # will be true if either is true
df3[unique]
