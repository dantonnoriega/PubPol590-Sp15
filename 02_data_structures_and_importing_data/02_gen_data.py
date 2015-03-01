import pandas as pd
import numpy as np
from pandas import *

df = DataFrame() # generate data frame


# create a stacked list (vector) with mean `a`, stddev `b`, and length `n`
# the idea here is to just create fake data
def norm_samp(a,b,n):
    u = np.random.randn
    l = [abs(b*u() + a) for i in xrange(n)]
    return l

# send in list of IDs where each ID is repeated and stacked `n` times
def stack_id(ids, n):
    y = [[x]*n for x in ids]
    return sum(y, [])

ids = [1,2,3,4] # id vector
t_size = 100    # length of time, t
s = stack_id(ids, t_size)   # get id stack
d = norm_samp(.15,1.2,len(s)) # get data stack
dates = pd. date_range('20130101', periods = t_size) # generate dates stack

# combine everything into a dataframe
df = pd.DataFrame({ 'panid' : s,
                    'date' : list(dates)*len(ids),
                    'consump' : d
                })

# arrange column order
df = df[[2,1,0]]

# export a csv copy without index
df.to_csv("/Users/dnoriega/Desktop/sample_data.csv", index = 0)
