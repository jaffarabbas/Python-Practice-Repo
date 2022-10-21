import pandas as pf

# df=pf.DataFrame({'a':[11,21,31],'b':[21,22,23]})
df=pf.DataFrame({'a':[1,2,1],'b':[1,1,1]})

# print(df['a'].unique())
# print(df['a']==1)
df.to_csv("file.csv")