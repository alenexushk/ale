import pandas as pd
from pandas_datareader import data, wb
import datetime

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2015, 1, 1)

att = data.DataReader("T", 'yahoo', start, end)

print(att.head)
print(50*"#")

# This keeps original column and displays
att['Open_original'] = att['Open']

# Here, if Open column exists, it will open it
# If not, it will create 

att['Open / 10'] = att['Open'] / 10

print(att.head())

att['High_minus_low'] = att['High'] - att['Low']

print(att.head)
