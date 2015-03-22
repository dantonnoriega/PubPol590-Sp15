from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm
import os

main_dir = "/Users/dnoriega/GitHub/Duke_PubPol590/"
root = main_dir + "/data/"
paths = [root + v for v in os.listdir(root) if v.startswith("08_")]

# IMPORT AND ADD/DROP VARIABLES ----------
df = pd.read_csv(paths[1], header=0, parse_dates=[1], date_parser=np.datetime64)
df_assign = pd.read_csv(paths[0], header=0)
df_assign.rename(columns={'assignment':'T'}, inplace=True)

"""NOTE: using notation from allcott 2010"""

# ADD/Drop Variables -----
ym = pd.DatetimeIndex(df['date']).to_period('M') # 'M'=month, 'D'=day etc.
df['ym'] = ym.values

# MONTHLY AGGREGATION --------
grp = df.groupby(['ym', 'panid'])
df = grp['kwh'].sum().reset_index()

# MERGE STATIC VARIABLES ------
df = pd.merge(df, df_assign)
df.reset_index(drop=True, inplace=True)

# FE MODEL (DEMEANING)

def demean(df, cols, panid):
    """
    inputs: df (pandas dataframe), cols (list of str of column names from df),
                    panid (str of panel ids)
    output: dataframe with values in df[cols] demeaned
    """

    from pandas import DataFrame
    import pandas as pd
    import numpy as np

    cols = [cols] if not isinstance(cols, list) else cols
    panid = [panid] if not isinstance(panid, list) else panid
    avg = df[panid + cols].groupby(panid).aggregate(np.mean).reset_index()
    cols_dm = [v + '_dm' for v in cols]
    avg.columns = panid + cols_dm
    df_dm = pd.merge(df[panid + cols], avg)
    df_dm = DataFrame(df[cols].values - df_dm[cols_dm].values, columns=cols)
    return df_dm

## set up variables for demeaning
df['log_kwh'] = df['kwh'].apply(np.log)
df['P'] = 0 + (df['ym'] > 541)
df['TP'] = df['T']*df['P']


# demean variables
cols = ['log_kwh', 'TP', 'P']
panid = 'panid'
df_dm = demean(df, cols, 'panid')

## set up regression variables
mu = pd.get_dummies(df['ym'], prefix = 'ym').iloc[:, 1:-1]
y = df_dm['log_kwh']
X = df_dm[['TP', 'P']]
X = sm.add_constant(X)

## run model
fe_model = sm.OLS(y, pd.concat([X, mu], axis = 1))
fe_results = fe_model.fit()
print(fe_results.summary())


