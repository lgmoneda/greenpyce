# greenpyce
Utilities for the Python data analysis library Pandas.

## Feature Engineering  
### Categorical
#### One-Hot Encoding
Apply onehot encoding to the passed columns
  
```python
onehot(df, columns, new_column=False)
```
  
```
    names  names_George  names_John  names_Paul  names_Ringo
0    Paul             0           0           1            0
1  George             1           0           0            0
2   Ringo             0           0           0            1
3   Ringo             0           0           0            1
4    John             0           1           0            0
5    John             0           1           0            0
6    John             0           1           0            0
```

#### Label Count  
Encodes categorical features as its count in the column.

```python
label_count(df, columns, new_column=False)
```

```
    names  names_labelcount
0    Paul                 1
1  George                 1
2   Ringo                 2
3   Ringo                 2
4    John                 3
5    John                 3
6    John                 3

```

#### Rank Categories	  

Encodes categories as its count rank

```python
rank_categorical(df, columns, inverse=False, new_column=False):
```
  
```
    names  names_rankcategorical
0    Paul                      4
1  George                      3
2   Ringo                      2
3   Ringo                      2
4    John                      1
5    John                      1
6    John                      1

```
  
#### Target Encoding	  

Encodes categories as its target mean

```python
te = TargetEncoder(columns, target)
te.fit(df)
te.transform(df)
```
  
```
    names  target  names_target_encoding
0    Paul      10                   10.0
1  George       2                    2.0
2   Ringo       4                    4.5
3   Ringo       5                    4.5
4    John       1                    2.0
5    John       3                    2.0
6    John       2                    2.0

```
