import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('2018WinterOlympics.csv')
# print(df)

# Normal bar chart
# data = [go.Bar(x=df['NOC'],
#                y=df['Total'])]
# layout = go.Layout(title='Medals')
# fig = go.Figure(data=data, layout=layout)
# pyo.plot(fig)

# Nested Bar chart
# trace1 = go.Bar(x=df['NOC'],
#                 y=df['Gold'],
#                 name='Gold',
#                 marker={'color':'#FFD700'})
#
# trace2 = go.Bar(x=df['NOC'],
#                 y=df['Silver'],
#                 name='Silver',
#                 marker={'color':'#9EA0A1'})
#
# trace3 = go.Bar(x=df['NOC'],
#                 y=df['Bronze'],
#                 name='Bronze',
#                 marker={'color':'#CD7F32'})
#
# data = [trace1,trace2,trace3]
# layout = go.Layout(title='Medals')
# fig = go.Figure(data=data, layout=layout)
# pyo.plot(fig)

# Stacked Bar Chart
trace1 = go.Bar(x=df['NOC'],
                y=df['Gold'],
                name='Gold',
                marker={'color':'#FFD700'})

trace2 = go.Bar(x=df['NOC'],
                y=df['Silver'],
                name='Silver',
                marker={'color':'#9EA0A1'})

trace3 = go.Bar(x=df['NOC'],
                y=df['Bronze'],
                name='Bronze',
                marker={'color':'#CD7F32'})

data = [trace1,trace2,trace3]
layout = go.Layout(title='Medals', barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
