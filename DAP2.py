
import pandas as pd

starting = {'Col_1':[5,2,4,7,2,4],
            'Col_2':[7,8,2,1,5,6],
            'Col_3':[10,4,2,1,8,2],
            'Col_4':[5,6,7,1,1,4],
            'Col_5':[9,9,2,1,5,2],
            'Col_6':[7,8,2,1,7,8],}

df = pd.DataFrame(starting)

#print(df.head()) # the first 5 rows of data
#print(df.tail()) # last 5 rows

#print(df.head(2)) # first 2 lines
#print(df.tail(2)) # last 2 lines

#print(df)

#print(df[2]) # this fails cause it looks for a column with 2 as header

print(df['Col_1'][2]) #->Looks for Col_1, value in segment 2. Cannot use
                      # negative number inside like -1
