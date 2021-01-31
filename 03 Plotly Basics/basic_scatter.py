# basic_scatter.py
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

# Our data
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

# Plotting the data
# data variable
# A list that contains the actual plot
data = [go.Scatter(x = random_x,
                   y = random_y,
                   mode='markers',
                   marker=dict(
                        size = 12,
                        color = 'rgb(51,204,153)',
                        symbol='pentagon',
                        line= {'width':2}
                   ))]

# layout variable
# not a list
# the x and y axis calls are equivalent. they don't have to be different
layout = go.Layout(title='Hello First Plot',
                    xaxis= {'title': 'MY X AXIS'},
                    yaxis= dict(title='MY Y AXIS'),
                    hovermode='closest')

# data and layout put into a figure object
fig = go.Figure(data=data,layout=layout)

# passing the figure object into a plot call
pyo.plot(fig, filename='scatter.html')
