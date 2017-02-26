import pytest
import pandas as pd

@pytest.fixture()
def default_cat_df():
    df = pd.DataFrame()
    df["names"] = ["Paul", "George", "Ringo", "Ringo", "John", "John", "John"]
    return df

    
