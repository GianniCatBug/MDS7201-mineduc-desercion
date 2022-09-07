import pandas as pd

def iter_df_read(file, col_name, condition_list, chunksize=1000, **kwargs):
    iter_csv = pd.read_csv(file, iterator=True, chunksize=chunksize, **kwargs)
    return pd.concat([chunk[chunk[col_name].isin(condition_list)] for chunk in iter_csv])