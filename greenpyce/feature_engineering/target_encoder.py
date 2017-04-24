import pandas as pd

class TargetEncoder(object):

    def __init__(self, columns, target):
        self.means_dict = {}
        self.columns = columns
        self.target = target
        
        for column in columns:
            self.means_dict[column] = {}

    
    def fit(self, df):

        for column in self.columns:
        
            group = pd.groupby(df[[column, self.target]], column).mean()
            self.means_dict[column] = group.to_dict()
            
    def transform(self, df):
        for column in self.columns:
            
            new_column_name = column
            # if new_column:
            #     new_column_name = column + "_target_encoding"
            df[new_column_name] = df[column].apply(lambda x : self.means_dict[column][self.target][x])
        
