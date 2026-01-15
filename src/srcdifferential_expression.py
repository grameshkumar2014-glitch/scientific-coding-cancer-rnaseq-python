import pandas as pd
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests

def run_differential_expression(counts, labels):
    tumor = counts.loc[:, labels == "tumor"]
    normal = counts.loc[:, labels == "normal"]

    stats, pvals = ttest_ind(tumor, normal, axis=1, equal_var=False)
    _, fdr, _, _ = multipletests(pvals, method="fdr_bh")

    results = pd.DataFrame({
        "statistic": stats,
        "pvalue": pvals,
        "fdr": fdr
    })
    return results