# greenpyce
Utilities for the Python data analysis library Pandas.

1. [Feature Engeering](#feature-engineering)  
    1. [Categorical](#categorical)  
         1. [One-Hot](#one-hot-encoding)  
         2. [Label Count](#label-count)  
         3. [Rank Categories](#rank-categories)  
         4. [Target Encoding](#target-encoding)  
    2. [Dates](#dates)  
         1. [Time Delta](#time-delta)  
		 2. [Expand Date](#expand-date)  
		 3. [Day of Week](#day-of-week)  
		 4. [Period of Day](#period-of-day)

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
lc = LabelCount(["names"])
lc.fit(df)
lc.transform(df)
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
rc = RankCategorical(["names"], inverse=False, new_column=False)
rc.fit(df)
rc.transform(df)
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
  
#### Target Encoding	  <a name="#target_encoding"> </a>

Encodes categories as its target mean

```python
te = TargetEncoder(["names"], "target")
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
### Dates
Feature creation based on date information  

#### Time Delta

#### Expand Date
