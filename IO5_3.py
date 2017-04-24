# Compare time for pandas vs pickle

import pandas as pd
import urllib.request
import pickle
import time

depth_json = urllib.request.urlopen('https://btc-e.com/api/3/depth/btc_usd').read()
depth_df = pd.read_json(depth_json)
depth_df.to_pickle('pickle.pickle')
newdf = pd.read_pickle('pickle.pickle')

# Using pandas to convert dataframe to pickle
# ('pickling' a dataframe)
pickle_out = open('newdf.pickle','wb') # 'write binary'
pickle.dump(newdf, pickle_out)
pickle_out.close()

pickle_in = open('newdf.pickle','rb') # 'read binary'
super_cool = pickle.load(pickle_in)

# How much time does this operation take?
start = time.time()
depth_df.to_pickle('pickle.pickle')
newdf = pd.read_pickle('pickle.pickle')
print(time.time()-start)

# How about this one?
start = time.time()
pickle_out = open('newdf.pickle','wb')
pickle.dump(newdf, pickle_out)
pickle_out.close()
pickle_in = open('newdf.pickle','rb') 
super_cool = pickle.load(pickle_in)
print(time.time()-start)
