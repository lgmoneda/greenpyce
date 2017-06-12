import numpy as np

def count_zeros(df, columns, new_col_name=None):

    if new_col_name == None:
        new_col_name = "row_stats_zeros_count"
    df[new_col_name] = df[columns].apply(lambda x: len(x) - np.count_nonzero(x), axis=1)

def count_non_zeros(df, columns, new_col_name=None):

    if new_col_name == None:
        new_col_name = "row_stats_non_zeros_count"
    df[new_col_name] = df[columns].apply(lambda x: np.count_nonzero(x), axis=1)

