import pytest
import pandas as pd

@pytest.fixture()
def default_cat_df():
    df = pd.DataFrame()
    df["names"] = ["Paul", "George", "Ringo", "Ringo", "John", "John", "John"]
    df["target"] = [10, 2, 4, 5, 1, 3, 2]
    return df

@pytest.fixture()
def default_num_df():
    df = pd.DataFrame()
    df["Column_1"] = [1, 0, 3, 5]
    df["Column_2"] = [0, 0, 2, 1]
    return df
