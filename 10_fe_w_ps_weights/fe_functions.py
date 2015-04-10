"""demean function"""

def demean(DF, panid):
    """
    inputs: df (pandas dataframe), panid = vector of ids
    output: dataframe with values in df demeaned
    """

    from pandas import DataFrame, Series
    import pandas as pd

    DF = pd.concat([panid, DF], axis=1)
    avg = DF.groupby(DF[panid.name]).mean().reset_index()
    avg = pd.merge(DF[panid.name].reset_index(), avg).drop('index', axis=1)
    avg = avg.drop(panid.name, axis=1)
    DF_dm = DF.drop(panid.name, axis=1)
    DF_diff = DF_dm.values - avg.values
    if DF_diff.shape[1] > 1:
        cols = DF_dm.columns
        DF_diff = DataFrame(DF_diff, columns = cols)
    else:
        cols = DF_dm.columns[0]
        DF_diff = Series(DF_diff.T[0])
        DF_diff.name = cols

    return DF_diff
