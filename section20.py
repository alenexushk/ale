import pandas as pd
from pandas_datareader import data, wb
import datetime

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2015, 1, 1)

att = data.DataReader("T", 'yahoo', start, end)

#print(att.head())
#print(50*"#")
describe = att.describe()
#print(describe)
#print(describe['Open'])

# Retrieve whole dataframe's StDev
print(describe['Open']['std'])