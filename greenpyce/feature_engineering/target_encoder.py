import pandas as pd
import numpy as np


class TargetEncoder(object):

    def __init__(self, columns, target, new_column=False):
        self.means_dict = {}
        self.columns = columns
        self.target = target
        self.new_column = new_column
            
    def fit(self, df):
        for column in self.columns:
            group = pd.groupby(df[[column, self.target]], column).mean()
            self.means_dict[column] = group.to_dict()
            
    def transform(self, df):
        for column in self.columns:
            
            new_column_name = column
            if self.new_column:
                new_column_name = column + "_target_encoding"
            
            missing = np.mean(np.array(self.means_dict[column][self.target].values()))
            df[new_column_name] = df[column].apply(lambda x : self.means_dict[column][self.target].get(x, missing))
        
                
