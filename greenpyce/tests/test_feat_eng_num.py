import sys
sys.path.append("../")
from _fixtures import *
import pandas as pd
import numpy as np
from feature_engineering.row_statistics import count_non_zeros
from feature_engineering.row_statistics import count_zeros

class Test_Num_Feat_Eng():

    def test_count_zeros(self, default_num_df):
        df = default_num_df
        
        count_non_zeros(df, ["Column_1", "Column_2"])
        assert (df["row_stats_non_zeros_count"].values == np.array([1, 0, 2, 2])).all()

        count_zeros(df, ["Column_1", "Column_2"])
        assert (df["row_stats_zeros_count"].values == np.array([1, 2, 0, 0])).all()
