import pandas as pd

def load_clean_XY(fpath_X, fpath_Y):
  # cols to drop from X_df
  drop_cols = ['id', 'num_private', 'construction_year', 'scheme_name', \
  'extraction_type', 'extraction_type_group', 'payment_type', 'water_quality', \
  'quantity_group', 'source', 'waterpoint_type_group']

  # loads X & y dfs
  X_df = pd.read_csv(fpath_X)
  y_df = pd.read_csv(fpath_Y)

  # X_df cleaning & feature engineering
  X_df['public_meeting'] = X_df['public_meeting'].replace({True: 1, False: 0})
  X_df['permit'] = X_df['permit'].replace({True: 1, False: 0})

  # y_df cleaning & feature engineering
  y_df['needs_repair'] = 1 * (y_df.status_group == 'functional')

  # Combines two dfs, dropping aforementioned cols
  comb_df = y_df.merge(X_df).drop(columns=drop_cols)

  # returns X & y
  return comb_df.drop(columns=['status_group', 'needs_repair']), comb_df.needs_repair, comb_df