import pandas as pd

df = pd.read_csv('business.csv')

#print(df.tail(5))

#read Headers -> 
#print(df.columns)

#read Column Values -> 
# print(df['State'])

# read column list ->
#print(df[['State', 'Year', 'Data.Calculated.Net Job Creation Rate', 'Data.Job Creation.Births', 'Data.Job Destruction.Rate']])

# read specific row(s) with Integer Location 
#print(df.iloc[1:4])

#read specific location(R,C)
print(df.iloc[2,1])
