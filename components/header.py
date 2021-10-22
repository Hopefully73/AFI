import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from index import app, server

title_div = html.Div(
    [
        html.H6("Dashboard", className="header_caption"),
        html.H1("Fun Flavor Games | Alien Food Invasion"),
    ]
)

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(width={"size": 1}),
                dbc.Col([title_div], width={"size": 7}),
                dbc.Col(width={"size": 1}),
            ],
            className="header_row",
        ),
    ],
    className="header_panel",
)