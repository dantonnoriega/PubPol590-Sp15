
# DEFINE FUNCTIONS -----------------
class logit_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def rm_perf_sep(y, X):

    import pandas as pd
    import numpy as np

    dep = y.copy()
    indep = X.copy()
    yx = pd.concat([dep, indep], axis = 1)
    grp = yx.groupby(dep)

    nm_y = dep.name
    nm_dum = np.array([v for v in indep.columns if v.startswith('D_')])

    DFs = [yx.ix[v,:] for k, v in grp.groups.iteritems()]
    kind = np.array([i for i, v in grp.groups.iteritems()]*2)

    perf_sep0 = np.ndarray((2, indep[nm_dum].shape[1]),
        buffer = np.array([np.linalg.norm(DF[nm_y].values.astype(bool) - v.values) for DF in DFs for k, v in DF[nm_dum].iteritems()]))
    perf_sep1 = np.ndarray((2, indep[nm_dum].shape[1]),
        buffer = np.array([np.linalg.norm(~DF[nm_y].values.astype(bool) - v.values) for DF in DFs for k, v in DF[nm_dum].iteritems()]))

    check = np.vstack([perf_sep0, perf_sep1])==0.
    indx = np.where(check)[1] if np.any(check) else np.array([])
    if indx.size > 1:
        kind = ['failure' if i == 0 else 'success' for i in kind[np.where(check)[0]]]
    else:
        kind = 'failure' if kind[np.where(check)[0]] == 0 else 'success'

    if indx.size > 0:
        keep = np.all(np.array([indep.columns.values != i for i in nm_dum[indx]]), axis=0)
        nms = [i.encode('utf-8') for i in nm_dum[indx]]
        print (logit_colors.FAIL + logit_colors.UNDERLINE +
        "\n%s perfectly predict %s.\nVariables and observations removed.\n" + logit_colors.ENDC) % (nms, kind)

        # return matrix with perfect predictor colums removed and obs where true
        indep1 = indep[np.all(indep[nm_dum[indx]]!=1, axis=1)].ix[:, keep]
        dep1 = dep[np.all(indep[nm_dum[indx]]!=1, axis=1)]
        return dep1, indep1
    else:
        return dep, indep


def rm_vif(X):

    import numpy as np

    import statsmodels.stats.outliers_influence as smso
    loop=True
    indep = X.copy()
    # print indep.shape
    while loop:
        vifs = np.array([smso.variance_inflation_factor(indep.values, i) for i in xrange(indep.shape[1])])
        max_vif = vifs[1:].max()
        # print max_vif, vifs.mean()
        if max_vif > 30 and vifs.mean() > 10:
            where_vif = vifs[1:].argmax() + 1
            keep = np.arange(indep.shape[1]) != where_vif
            nms = indep.columns.values[where_vif].encode('utf-8') # only ever length 1, so convert unicode
            print (logit_colors.FAIL + logit_colors.UNDERLINE +
            "\n%s removed due to multicollinearity.\n" + logit_colors.ENDC) % nms
            indep = indep.ix[:, keep]
        else:
            loop=False
    # print indep.shape

    return indep

## returns logit_results and final DataFrame
def do_logit(df, tar, stim, add_D=None, mc=False):

    import pandas as pd
    import statsmodels.api as sm

    DF = df.copy()
    if add_D is not None:
        DF = pd.merge(DF, add_D, on = 'ID')
        kwh_cols = [v for v in DF.columns.values if v.startswith('kwh')]
        dum_cols = [v for v in add_D.columns.values if v.startswith('D_')]
        cols = kwh_cols + dum_cols
    else:
        kwh_cols = [v for v in DF.columns.values if v.startswith('kwh')]
        dum_cols = [v for v in DF.columns.values if v.startswith('D_')]
        cols = kwh_cols + dum_cols

    # DF.to_csv("/Users/dnoriega/Desktop/" + "test.csv", index = False)
    # set up y and X
    indx = (DF.tariff == 'E') | ((DF.tariff == tar) & (DF.stimulus == stim))
    df1 = DF.ix[indx, :].copy() # `:` denotes ALL columns; use copy to create a NEW frame
    df1['T'] = 0 + (df1['tariff'] != 'E') # stays zero unless NOT of part of control
    # print df1

    y = df1['T']
    X = df1[cols] # extend list of kwh names
    X = sm.add_constant(X)

    msg = ("\n\n\n\n\n-----------------------------------------------------------------\n"
    "LOGIT where Treatment is Tariff = %s, Stimulus = %s"
    "\n-----------------------------------------------------------------\n") % (tar, stim)
    print msg

    print (logit_colors.FAIL +
        "\n\n-----------------------------------------------------------------" + logit_colors.ENDC)

    y, X = rm_perf_sep(y, X) # remove perfect predictors
    X = rm_vif(X) if mc else X # remove multicollinear vars

    print (logit_colors.FAIL +
        "-----------------------------------------------------------------\n\n\n" + logit_colors.ENDC)

    ## RUN LOGIT
    logit_model = sm.Logit(y, X) # linearly prob model
    logit_results = logit_model.fit(maxiter=1000, method='newton') # get the fitted values
    print logit_results.summary() # print pretty results (no results given lack of obs)

    return logit_results, DF.ix[X.index, :]
