import pandas as pd
import numpy as np

def onehot(df, columns, new_columns=False):
    """
    Apply onehot encoding to the passed columns
    """
    dummies = pd.get_dummies(df, columns=columns)
    return pd.concat([df, dummies], axis=1)
    
def rank_categorical(df, columns, inverse=False, new_column=False):
    """
    Encodes categories as its count rank
    """
    for column in columns:
        count = df[column].value_counts()
        print(count)
        if inverse:
            count = count.sort_values()
        ranks = [i for i in range(1, count.shape[0] + 1)]
        count = pd.DataFrame(ranks, index=count.index.values)
        new_column_name = column
        if new_column:
            new_column_name = column + "_rankcategorical"
        df[new_column_name] = df[column].apply(lambda x : count[count.index == x].values[0][0])
        print(df)
        
    return df

def label_count(df, columns, new_column=False):
    """
    Encodes categorical features as its count in the column.
    """
    for column in columns:
        count = df[column].value_counts()
        new_column_name = column
        if new_column:
            new_column_name = column + "_labelcount"
        df[new_column_name] = df[column].apply(lambda x : count[count.index == x].values[0])

    return df



