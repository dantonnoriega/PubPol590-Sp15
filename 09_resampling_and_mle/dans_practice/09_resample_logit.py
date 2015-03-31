## group task 3 practice
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os


main_dir = "/Users/dnoriega/Dropbox/PubPol590_Sp15/"
root = main_dir + "data_sets/CER/tasks/"

df_alloc = pd.read_csv(root + "allocation_subsamp.csv")

ids = df_alloc['ID']

