import pickle
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pickle.load(open("patient_data.pkl", "rb"))

app = dash.Dash(__name__)
fig = px.histogram(df, x="BP", title="Blood Pressure Distribution")

app.layout = html.Div([
    html.H1("Health Monitoring System", style={'textAlign': 'center', 'color': 'white', 'backgroundColor': '#2c3e50', 'padding': '10px'}),
    dcc.Graph(figure=fig),
])

if __name__ == "__main__":
    app.run_server(debug=True)
