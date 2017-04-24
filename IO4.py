# About JSON

import pandas as pd
import urllib.request

df = pd.read_hdf('hdfstore.h5','d1')

# print(df.head())

# write to json file
# this created a sort of python dictionary
df.to_json('example_json.json')

#bring json back
df2 = pd.read_json('example_json.json')
#print(df2.head)

#sample JSON here:
# https://btc-e.com/api/3/depth/btc_usd

depth_json = urllib.request.urlopen('https://btc-e.com/api/3/depth/btc_usd').read()

depth_df = pd.read_json(depth_json)

print(depth_json)

