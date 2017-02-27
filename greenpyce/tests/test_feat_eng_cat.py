import sys
sys.path.append("../")
from feature_engineering.categorical import *
from _fixtures import *
import pandas as pd
import numpy as np


class Test_Categorical_Feat_Eng():

    def test_onehot(self, default_cat_df):
        df = default_cat_df
        df = onehot(default_cat_df, ["names"])
        
        assert np.all(df["names_John"].values == np.array([0, 0, 0, 0, 1, 1, 1])), "encoding error"       
        assert np.all(df["names_Ringo"].values == np.array([0, 0, 1, 1,0,0,0])), "onehot encoding error"
        assert np.all(df["names_Paul"].values == np.array([1, 0, 0, 0,0,0,0])), "onehot encoding error"
        assert np.all(df["names_George"].values == np.array([0, 1, 0, 0, 0, 0, 0])), "onehot encoding error"    

    def test_count(self, default_cat_df):
        df = default_cat_df 
        
        assert np.all(label_count(df, ["names"])["names"].values == np.array([1, 1, 2, 2, 3, 3, 3])), "LabelCount not working"
    def test_rank(self, default_cat_df):
        df = default_cat_df
        
        assert np.all(rank_categorical(df, ["names"])["names"].values == np.array([4, 3, 2, 2, 1, 1, 1])), "RankCategorical not working"

    def test_target_encoding(self, default_cat_df):
        df = default_cat_df
        pytest.set_trace()        
        df = target_encoding(df, ["names"], "target", new_column=True)

        assert np.all(df["names"].values == np.array([10, 2, 4.5, 4.5, 2, 2, 2]))
