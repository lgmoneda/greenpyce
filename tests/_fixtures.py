import pytest
import pandas as pd

@pytest.fixture()
def default_cat_df():
    df = pd.DataFrame()
    df["names"] = ["Paul", "George", "Ringo", "Ringo", "John", "John", "John"]
    df["target"] = [10, 2, 4, 5, 1, 3, 2]
    return df

    
