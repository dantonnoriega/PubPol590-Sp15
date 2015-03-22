"""demean function"""

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


def se_cluster(fe_results, df, group):

    """
    degrees of freedom adjustment for nested-within-cluster std. err.
        see http://www.stata.com/statalist/archive/2013-01/msg00596.html
    """
    from numpy.linalg import matrix_rank
    from statsmodels.stats.sandwich_covariance import cov_cluster

    cl_se = np.sqrt(cov_cluster(fe_results, df[group]).diagonal())
    cols = [v for v in X.columns if not v.startswith("panid")]
    V = fe_results.cov_params().ix[cols, cols]
    N = fe_results.nobs
    N_grp = len(np.unique(df[group].squeeze()))
    rank = matrix_rank(V)
    df_cl = N - (rank - 1) - (N_grp - 1) # degrees of freedom for cluster-robust but no nested adjustmnet
    df_xt = N - (rank - 1) # degrees of freedom for cluster-nested-robust
    cl_se_adj = cl_se * np.sqrt(df_cl/df_xt)
    return cl_se_adj
