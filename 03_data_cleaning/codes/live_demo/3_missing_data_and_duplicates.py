from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/dnoriega/Desktop/pubpol590_data"
git_dir = "/Users/dnoriega/Desktop/pubpol590"
csv_file = "sample_data_unclean.csv"

# IMPORT DATA -----------------------------

df = pd.read_csv(os.path.join(main_dir, csv_file))

list_of_types = [ isinstance(v, int )]