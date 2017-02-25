import sys
sys.path.append("../")
from feature_engineering.categorical import *
import pandas as pd
import numpy as np


class Test_Categorical_Feat_Eng():
    
    def test_count_rank_categorical(self):
        df = pd.DataFrame()
        df["names"] = ["Paul", "George", "Ringo", "Ringo", "John", "John", "John"]
        assert np.all(LabelCount(df, ["names"])["names"].values == np.array([1, 1, 2, 2, 3, 3, 3])), "LabelCount not working"

        df = pd.DataFrame()
        df["names"] = ["Paul", "George", "Ringo", "Ringo", "John", "John", "John"]
        assert np.all(RankCategorical(df, ["names"])["names"].values == np.array([4, 3, 2, 2, 1, 1, 1])), "RankCategorical not working"
