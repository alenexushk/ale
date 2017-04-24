#HDF - Hierarchical Data Format

import pandas as pd

df = pd.read_csv('newcsv4.csv', names=['Date', 'Violent_Crime_Rate'],
                 index_col = 0)
print(df.head())

# Create storage for HDF file
store = pd.HDFStore('hdfstore.h5')
print(store)

store.put('d1', df, format='table', data_columns=True)
# d1 equals the df defined in row 5
# How many rows, and how many columns
print(store['d1'].shape)
store.close()

# how to open and read a file
hdf = pd.read_hdf('hdfstore.h5','d1')

print(hdf)
