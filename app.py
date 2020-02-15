import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import pickle

#Initiate app
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
app.title='Internet Archive Author Prediction'

#Layout
app.layout = html.Div(children=[
    html.H1('Author Classification w/ Internet Archive'),
    html.Div([
        html.H6('Input Sample text here (at least 20 chars):'),
        dcc.Textarea(
            id='text-input',
            placeholder='Try out a text sample!',
        ),
        html.H6(id='output-message', children='output will go here')

    ]),
    html.Br(),
    html.A('Code on github:', href='https://github.com/tallywiesenberg/Predict-the-Philosopher')
])
#Execute the app
if __name__ == "__main__":
    app.run_server()