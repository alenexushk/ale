# Pickles allow you to store in
# binary form, making things faster

import pandas as pd
import urllib.request
import pickle

depth_json = urllib.request.urlopen('https://btc-e.com/api/3/depth/btc_usd').read()
depth_df = pd.read_json(depth_json)

print(depth_json)

# Convert to Pickle
depth_df.to_pickle('pickle.pickle')

# Load pickle into a dataframe

newdf = pd.read_pickle('pickle.pickle')

print(newdf)