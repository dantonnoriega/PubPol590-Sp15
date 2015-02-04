from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/dnoriega/Desktop/pubpol590_data"
csv_file = "small_data_w_missing_duplicated.csv"

# IMPORT DATA ---------------------------------------
df = pd.read_csv(os.path.join(main_dir, csv_file), na_values = ['-', 'NA'])

# DROP DUPS -----------------------------
df1 = df.drop_duplicates()

# EXPLORE DATA ------------------------------
df1[df1.consump.isnull()] # investigate data where 'consump' is empty (null)

df1[df1.duplicated(['panid', 'date'])] # look at duplicated (first hit from top-bottom) using 'panid' and 'date' as criteria
df1[df1.duplicated(['panid', 'date'], take_last = True)] # same but bottom to top

df2 = df1.drop_duplicates(['panid', 'date'], take_last = True) # this will keep the bottom to top

df2[df2.duplicated(['panid', 'date'])] # check for dups. its empty!

df2.consump.mean() # get mean