import pandas as pd
import numpy as np

class EntityEmbedding(object):
    """
    Maps integers to vectors.
    """
    def __init__(self, output_dim_dict, target):
        self.output_dim_dict = output_dim_dict
        self.columns = output_dim_dict.keys()
        self.target = target

        for column in columns:
            self._models[column] = {}
        self._build_models

        
    def _build_model:
        from keras import Sequential
        model = Sequential()
        model.add(Embedding(self.max_int))
        model.compile('rmsprop', 'mse')
        self._model = model
        
    def fit(self, df):
        self._model.fit()
        for column in self.columns:
        
            group = pd.groupby(df[[column, self.target]], column).mean()
            self.means_dict[column] = group.to_dict()
            
    def transform(self, df):
        for column in self.columns:
            
            new_column_name = column
            # if new_column:
            #     new_column_name = column + "_target_encoding"
            
            missing = np.mean(np.array(self.means_dict[column][self.target].values()))
            df.loc[:, new_column_name] = df[column].apply(lambda x : self.means_dict[column][self.target].get(x, missing))
        
