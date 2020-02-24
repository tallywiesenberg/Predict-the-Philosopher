import db
from db import load_data, populate_table
import pickles
from pickles import load_knn, load_nb
import words
from words import tokenize
from words import get_doc_vectors, load_2d_vectors
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly_express as px
import pickle

#Initiate app
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
app.title='Michel Foucault vs. Noam Chomksy Author Prediction'

#Populate Database
df = load_data()
# populate_table()

#Load 2D Vectors for Graph
vectors = load_2d_vectors()

#Layout
app.layout = html.Div(children=[
    html.H1('Author Classification: Foucault or Chomsky'),
    html.Div([
        html.H6('Input Sample text here (at least 20 chars):'),
        dcc.Textarea(
            id='text-input',
            placeholder='Try out a text sample!',
        ),
        html.Br(),
        html.H6(id='output-message', children='output will go here'),
        html.Br(),
        html.H3('Document Vectors in Two Dimensions Colored by Author'),
        dcc.Graph(
            id='graph', style={'width': '50%', 'display': 'inline-block'},
            figure=px.scatter(
                x=vectors[:,0], y=vectors[:,1], color=df['author']
            ))
    ]),
    html.Br(),
    html.A('Code on github:', href='https://github.com/tallywiesenberg/Predict-the-Philosopher')
])

#Ineractive callbacks

@app.callback(
    Output('output-message', 'children'),
    [Input('text-input', 'value')]
    )
def display_results(text):
    if len(text) < 20:
        pass
    else:
        #Load models
        nb = load_nb()
        knn = load_knn()
        #Nearest Sample
        pred = nb.predict([text])
        vector = get_doc_vectors(text)
        new_obs = vector.reshape(1, -1)
        new_obs_2d = knn.named_steps['pca'].transform(new_obs)
        index = knn.named_steps['kneighborsclassifier'].kneighbors(new_obs_2d)[1][0][0]
        nn = df['extracts'][index]
        #Predict Authorship
        pred = nb.predict([text])[0]
        return f'The author most likely to have written your sample, "{text}", is {pred}. \n The most similar sample from the collection is "{nn}"'

# @app.callback(Output("graph", "figure"), [Input()])

#Execute the app
if __name__ == "__main__":
    
    app.run_server()