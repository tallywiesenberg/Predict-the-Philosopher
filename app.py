import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import pickle
import spacy
nlp = spacy.load("en_core_web_lg")
#Initiate app
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
app.title='Internet Archive Author Prediction'

#Layout
app.layout = html.Div(children=[
    html.H1('Author Classification: Foucault or Chomsky'),
    html.Div([
        html.H6('Input Sample text here (at least 20 chars):'),
        dcc.Textarea(
            id='text-input',
            placeholder='Try out a text sample!',
        ),
        html.H6('# of Neighbors'),
        html.Br(),
        dcc.Dropdown(
            id='k-drop',
            options=[{'label':i, 'value':i} for i in range(5, 25, 5)],
            value=5
        ),
        html.H6(id='output-message', children='output will go here')

    ]),
    html.Br(),
    html.A('Code on github:', href='https://github.com/tallywiesenberg/Predict-the-Philosopher')
])


#Ineractive callbacks

def get_doc_vectors(words):
    # converts a doc into a vector
    return nlp(words).vector

@app.callback(
    Output('output-message', 'children'),
    [Input('text-input', 'value'),
     Input('k-drop', 'value')]
    )
def display_results(text, k):
    file = open(f'./models/model_k{k}.pkl', 'rb')
    model = pickle.load(file)
    file.close()
    vector = get_doc_vectors(text)
    pred = model.predict(vector.reshape(1, -1))[0]
    return f'The author most likely to have written your sample, "{text}", is {pred}.'

#Execute the app
if __name__ == "__main__":
    app.run_server()