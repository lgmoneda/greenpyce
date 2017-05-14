import pandas as pd

class RankCategorical(object):

    def __init__(self, columns, new_column=False, inverse=False):
        self.rank_dict = {}
        self.columns = columns
        self.new_column = new_column
        self.inverse = inverse
        
        for column in columns:
            self.rank_dict[column] = {}

    
    def fit(self, df):

        for column in self.columns:
            count = df[column].value_counts()

            if self.inverse:
                count = count.sort_values()
            ranks = [i for i in range(1, count.shape[0] + 1)]
            count = pd.DataFrame(ranks, index=count.index.values)
            self.rank_dict[column] = count
        
    def transform(self, df):
        for column in self.columns:
            
            new_column_name = column
            
            if self.new_column:
                new_column_name = column + "_rankcategorical"

            missing = len(self.rank_dict) / 2
                        
            df[new_column_name] = df[column].apply(lambda x : self.rank_dict[column].ix[x].values[0])

                

        


        
