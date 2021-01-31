#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

data = [go.Scatter(x=df[df['DAY']==day]['LST_TIME'],
           y=df[df['DAY']==day]['T_HR_AVG'],
           mode='lines',
           name = day) for day in days]

layout = go.Layout(title='Daily Temperatures')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
