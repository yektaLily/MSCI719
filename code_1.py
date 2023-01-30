import dash
from dash import dcc
from dash import html
import plotly
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd 

df = pd.read_csv('datedData.csv')
df_m = pd.read_csv('mData.csv')
df_w = pd.read_csv('wData.csv')

#define the time options and data sets 
time_option = ['yearly', 'weekly', 'daily', 'monthly']

#build the app 
app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id = 'graph'),
    dcc.Dropdown(id = 'time-pick',
    options= time_option)
])

@app.callback(Output(component_id='graph', component_property='figure'),
              [Input(component_id='time-pick', component_property='value')]
)
def update_figure(freq_picked):

    if freq_picked == 'yearly':
        x_ = df['Date_']
    elif freq_picked == 'weekly':
        x_ = df_w['Date_']
    elif freq_picked == 'monthly': 
        x_ = df_m['Date_']
    elif freq_picked == 'daily':
        x_ = df['Day']
    else:
        x_ = df['Date_']

    flavor_options = ['Hazelnut St', 'Mango St','Green Tea St','Mint Choco']
    # flavor_names = ['Hazelnut', 'Mango', 'Green Tea', 'Mint Chocolate']

    traces = [] 
    for flavor in flavor_options: 
        traces.append(go.Scatter(
            x = x_, 
            y = df[flavor], 
            mode = 'lines', 
            name = flavor,
            opacity= 0.7,
            marker={'size': 12}
            )
        )

    fig = go.Figure({
        'data': traces,
        'layout': go.Layout(title = 'Ice-cream Flavor sales', 
                            xaxis= {'title': 'Time'},
                            yaxis={'title': 'Sales'}
        )
    })
    return fig 

if __name__ == '__main__':
    app.run_server()
