# basic-line2.py
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# US census data
df=pd.read_csv('nst-est2017-alldata.csv')

df2 = df[df['DIVISION'] =='1']
# grabs a col in df2 and sets it as index
df2.set_index('NAME', inplace=True)

# only want population columns
list_of_pop_cols = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_pop_cols]

# Going to use list comprehension to build traces
data = [go.Scatter(x=df2.columns,
                   y=df2.loc[name],
                   mode='lines',
                   name=name) for name in df2.index]

pyo.plot(data)
