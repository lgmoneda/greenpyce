# greenpyce
Utilities for the Python data analysis library Pandas

## Feature Engineering  
### Categorical  
#### LabelCount  
Encodes categorical features as its count in the column.

```python
LabelCount(df, columns, new_column=False)
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

#### LabelCount  

Encodes categories as its count rank

```python
RankCategorical(df, columns, inverse=False, new_column=False):
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