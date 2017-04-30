import sys
sys.path.append("../")
from feature_engineering.categorical import *
from _fixtures import *
import pandas as pd
import numpy as np
from feature_engineering.target_encoder import TargetEncoder
from feature_engineering.rank_categorical import RankCategorical
from feature_engineering.label_count import LabelCount
from feature_engineering.date import time_count_between_dates

class Test_Categorical_Feat_Eng():

    def test_onehot(self, default_cat_df):
        df = default_cat_df
        df = onehot(default_cat_df, ["names"], drop_first=False)
        
        assert np.all(df["names_John"].values == np.array([0, 0, 0, 0, 1, 1, 1])), "encoding error"       
        assert np.all(df["names_Ringo"].values == np.array([0, 0, 1, 1,0,0,0])), "onehot encoding error"
        assert np.all(df["names_Paul"].values == np.array([1, 0, 0, 0,0,0,0])), "onehot encoding error"
        assert np.all(df["names_George"].values == np.array([0, 1, 0, 0, 0, 0, 0])), "onehot encoding error"    

    def test_count(self, default_cat_df):
        df = default_cat_df 

        lc = LabelCount(["names"])
        lc.fit(df)
        lc.transform(df)

        assert np.all(df["names"].values == np.array([1, 1, 2, 2, 3, 3, 3])), "LabelCount not working"

    def test_rank(self, default_cat_df):
        df = default_cat_df

        rc = RankCategorical(["names"])
        rc.fit(df)
        rc.transform(df)
        
        assert np.all(df["names"].values == np.array([4, 3, 2, 2, 1, 1, 1])), "RankCategorical not working"

    def test_target_encoding(self, default_cat_df):
        df = default_cat_df
        
        te = TargetEncoder(["names"], "target")
        te.fit(df)
        te.transform(df)
        
        assert np.all(df["names"].values == np.array([10, 2, 4.5, 4.5, 2, 2, 2]))
