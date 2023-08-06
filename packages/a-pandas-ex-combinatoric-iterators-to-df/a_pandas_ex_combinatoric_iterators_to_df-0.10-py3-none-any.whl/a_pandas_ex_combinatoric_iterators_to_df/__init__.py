from a_pandas_ex_less_memory_more_speed import pd_add_less_memory_more_speed
pd_add_less_memory_more_speed()
from itertools import product,permutations,combinations,combinations_with_replacement
import pandas as pd
def _converter(list_, n, func):
    pdseriescheck = pd.Series(list_).to_frame()#.T
    dtypes=pdseriescheck.ds_reduce_memory_size(verbose=False).dtypes
    if func.__name__ == 'product':
        permu = func(list_, repeat=n)
    else:
        permu = func(list_,n)
    dtype=dtypes.astype('string').unique().tolist()
    df = pd.DataFrame(permu,dtype=dtype[0])
    return df
def product_to_df(iterable,n):
    return _converter(iterable, n, func=product)
def permutations_to_df(iterable,n):
    return _converter(iterable, n, func=permutations)
def combinations_to_df(iterable,n):
    return _converter(iterable, n, func=combinations)
def combinations_with_replacement_to_df(iterable,n):
    return _converter(iterable, n, func=combinations_with_replacement)
def pd_add_combinatoric_iterators_to_df():
    pd.Q_product_to_df = product_to_df
    pd.Q_permutations_to_df = permutations_to_df
    pd.Q_combinations_to_df = combinations_to_df
    pd.Q_combinations_with_replacement_to_df = combinations_with_replacement_to_df
