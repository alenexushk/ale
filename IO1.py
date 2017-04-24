import pandas as pd

df = pd.read_csv('FBI_CRIME11.csv')

df['Violent Crime Rate'].to_csv('newcsv2.csv')

df.set_index('Year', inplace = True) #modify the DF without having to redefine(df = ...)

print(df.head())

df['Violent Crime Rate'].to_csv('newcsv2.csv')
