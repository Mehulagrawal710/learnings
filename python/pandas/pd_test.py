import numpy as np
import pandas as pd

print("###reading data from csv###")
filename = 'pd.txt'
df = pd.read_csv(filename)
print(df)
print("##############")

print("###printing head/tail###")
print(df.head(1))
(df.tail(2))
print("##############")

print("###table contents###")
print(df.dtypes)
print(df.index)
print(df.columns)
print(df.values)
print("##############")

print("###count,mean,std,min,25%,50%,75%,max####")
print(df.describe())
print("##############")

print("##sort by any column###")
print(df.sort_values('c3', ascending=False))
print("##############")

print("##slicing records#####")
print(df.c2)
print(df['c2'])
print(df[2:3])
print(df[['c1','c3']]) #specified columns will be printed
print(df.loc[2:2,['c1', 'c2']])
print(df.loc[2, ['c2']])
print("##############")

print("###filtering  values###")
print(df[df.c2 > 2])
print(df[df['month'].isin(['jan', 'feb'])])
print("##############")

print("###assignment values###")
df.loc[2, ['c1']] = 101
print(df)
df.loc[1, ['c2']] = np.nan
print(df)
df.loc[:, 'c2'] = np.array([101]*len(df))
print(df)
df['c4'] = [101, 102, 103]
print(df)
print("##############")

print("###rename columns###")
df.columns = ['month', 'col1', 'col2', 'col3', 'col4']
print(df)
df.rename(columns = {'col1':'c1'}, inplace = True)
print(df)
print("##############")

print("###iterate a df###")
for index, row in df.iterrows():
	print(index, row['c1'], row['col2'])
print("##############")

print("###writing to csv file###")
df.to_csv('testwrite.csv')
df.to_excel('testwrite.xls')
print("##############")