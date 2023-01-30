import dash
from dash import dcc
from dash import html
import plotly
import plotly.offline as pyo 
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd 

df = pd.read_csv('datedData.csv')

time_option = ['yearly', 'weekly', 'daily', 'monthly']

app = dash.Dash()

trace0 = go.Scatter(x = df['Date_'], y = df['Green Tea St'], mode = 'lines', name = 'green tea')
trace1 = go.Scatter(x = df['Date_'], y = df['Hazelnut St'], mode = 'lines', name = 'Hazelnut')
trace2 = go.Scatter(x = df['Date_'], y = df['Mango St'], mode = 'lines', name = 'Mango')
trace3 = go.Scatter(x = df['Date_'], y = df['Mint Choco'], mode = 'lines', name = 'Mint Chocolate')


#data is always a list 
data = [trace0, trace1, trace2, trace3]

layout = go.Layout(title='Line Chart of flavors')
fig = go.Figure(data = data, layout= layout)

pyo.plot(fig, filename='line.html')