from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# IMPORTING DATA -----------------------------------------

## assigning file paths
main_dir = "/Users/dnoriega/Dropbox/PubPol590_Sp15"
txt_file = "/data_sets/File1_small.txt"

## import data
df = pd.read_table(main_dir + txt_file, sep = "\s")

## extract rows 60 to 99
df[60:100]

## extract rows where consumption (kwh) is > 30
df[df.kwh > 30]