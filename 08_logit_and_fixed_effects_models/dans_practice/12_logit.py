from __future__ import division
import pandas as pd
import numpy as np
import os

main_dir = "/Users/dnoriega/Dropbox/pubpol590_sp15/Grades/"

paths = [main_dir + v for v in os.listdir(main_dir)]

cat = pd.read_csv(paths[0], header=0)
cat.dropna(thresh=2, inplace=True)
sakai = pd.read_csv(paths[1], header=0)

sakai_cat = pd.merge(cat, sakai, 'outer')





