import numpy as np
import pandas as pd

# df = pd.read_csv('salaries.csv')
# print(df['Salary'].min())

# Only want to select rows where age > 30
# ser_of_bool = df['Age'] > 30
# print(ser_of_bool)
# print('')
# print(df[ser_of_bool])
# Typically done as one step
# print(df[df['Age'] > 30])
# print(df['Age'].unique())
# print(df['Age'].nunique())
# print(df.columns)
# print(df.info())
# print(df.describe())

# Going to make some dataframes using numpy generated numbers
mat = np.arange(0,10).reshape(5,2)
df = pd.DataFrame(data=mat, columns=['A','B'])
print(df)
