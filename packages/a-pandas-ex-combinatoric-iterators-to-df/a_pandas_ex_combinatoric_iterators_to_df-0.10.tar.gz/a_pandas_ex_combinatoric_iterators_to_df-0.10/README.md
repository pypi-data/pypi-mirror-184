# Creates DataFrames from product, permutations, combinations, combinations_with_replacement with best dtype

```python
# Tested with:
# Python 3.9.13
# Windows 10

pip install a-pandas-ex-combinatoric-iterators-to-df


from a_pandas_ex_combinatoric_iterators_to_df import pd_add_combinatoric_iterators_to_df
import pandas as pd
pd_add_combinatoric_iterators_to_df()

df1=pd.Q_product_to_df(iterable=list(range(256)), n=3)
df1
Out[3]: 

            0    1    2
0           0    0    0
1           0    0    1
2           0    0    2
3           0    0    3
4           0    0    4
       ...  ...  ...
16777211  255  255  251
16777212  255  255  252
16777213  255  255  253
16777214  255  255  254
16777215  255  255  255
[16777216 rows x 3 columns]

df1.dtypes
Out[4]: 
0    uint8
1    uint8
2    uint8
dtype: object


df2=pd.Q_permutations_to_df(iterable=list(range(256)), n=3)
df2
Out[5]: 
            0    1    2
0           0    1    2
1           0    1    3
2           0    1    4
3           0    1    5
4           0    1    6
       ...  ...  ...
16581115  255  254  249
16581116  255  254  250
16581117  255  254  251
16581118  255  254  252
16581119  255  254  253
[16581120 rows x 3 columns]


df3=pd.Q_combinations_to_df(iterable=list(range(256)), n=3)
df3
Out[6]: 
           0    1    2
0          0    1    2
1          0    1    3
2          0    1    4
3          0    1    5
4          0    1    6
      ...  ...  ...
2763515  251  254  255
2763516  252  253  254
2763517  252  253  255
2763518  252  254  255
2763519  253  254  255
[2763520 rows x 3 columns]

df4=pd.Q_combinations_with_replacement_to_df(iterable=list(range(256)), n=3)
df4
Out[7]: 
           0    1    2
0          0    0    0
1          0    0    1
2          0    0    2
3          0    0    3
4          0    0    4
      ...  ...  ...
2829051  253  255  255
2829052  254  254  254
2829053  254  254  255
2829054  254  255  255
2829055  255  255  255
[2829056 rows x 3 columns]

"""



```



