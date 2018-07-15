import pandas as pd

class LabelCount(object):

    def __init__(self, columns, new_column=False):
        self.count_dict = {}
        self.columns = columns
        self.new_column = new_column
        
    
    def fit(self, df):

        for column in self.columns:
            count = df[column].value_counts()
            
            self.count_dict[column] = count.to_dict()
        
    def transform(self, df):
        for column in self.columns:
            
            new_column_name = column
            
            if self.new_column:
                new_column_name = column + "_label_count"

            missing = 1
            df.loc[:, new_column_name] = df[column].apply(lambda x : self.count_dict[column].get(x, missing))            


        


        
