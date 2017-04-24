import pandas as pd

df = pd.read_csv('FBI_CRIME11.csv')

df['Violent Crime Rate'].to_csv('newcsv2.csv')

df.set_index('Year', inplace = True) #modify the DF without having to redefine(df = ...)

#print(df.head())

df['Violent Crime Rate'].to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv')
#print(df.head())

df = pd.read_csv('newcsv2.csv', index_col=0)
#print(df.head())

# Give names to columns. This is the key part for this tutorial..
df = pd.read_csv('newcsv2.csv', names = ['Date','Violent Crime Rate'],
                 index_col=0)
#print(df.head())

df.to_csv('newcsv3.csv')

df.to_csv('newcsv4.csv', header = False) # True/False for headers
