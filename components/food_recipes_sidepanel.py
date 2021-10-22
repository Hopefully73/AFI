import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import math
import time
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from index import app
from components import functions

df = pd.read_csv("data/food_recipes.csv")
df["Names"] = df["Food Recipe"].apply(functions.markdown_to_text)
x = df["Names"].unique()
x.sort()

search_div = html.Div(
    [
        html.H6("Search food recipe"),
        dcc.Dropdown(
            id="food-recipe-dropdown",
            options=[{'label': i, 'value': i} for i in x],
            persistence=True,
            persistence_type="memory",
            multi = True,
            placeholder = "Choose one or more from the list."
        ),
    ],
    className="input_div",
)

tier_div = html.Div(
    [
        html.H6("Select tier"),
        dbc.Checklist(
            options=[
                {"label": "1", "value": 1},
                {"label": "2", "value": 2},
                {"label": "3", "value": 3},
                {"label": "4", "value": 4}
            ],
            value=[1, 2, 3, 4],
            id="food-recipe-tier-checklist",
            inline=True,
            persistence=True,
            persistence_type="memory"
        )
    ],
    style={'font-family': 'Noto Sans'}
)

rarity_div = html.Div(
    [
        html.H6("Select rarity"),
        dbc.Checklist(
            options=[
                {"label": "Common", "value": "Common"},
                {"label": "Popular", "value": "Popular"},
                {"label": "Idolized", "value": "Idolized"}
            ],
            value=["Common", "Popular", "Idolized"],
            id="food-recipe-rarity-checklist",
            inline=True,
            persistence=True,
            persistence_type="memory",
        ),
    ],
    style={'font-family': 'Noto Sans'}
)

availability_div = html.Div(
    [
        html.H6("Select availability"),
        dbc.RadioItems(
            options=[
                {"label": "Free", "value": "free"},
                {"label": "Paid", "value": "paid"},
                {"label": "Both", "value": "both"}
            ],
            value="both",
            id="food-recipe-availability-radio",
            inline=True,
            persistence=True,
            persistence_type="memory"
        ),
    ],
    style={'font-family': 'Noto Sans'}
)

layout = dbc.Container(
    [
        dbc.Col(
            [
                dbc.Row(
                    [
                        dbc.Col(search_div),
                    ]
                ),
                html.H6(""),
                dbc.Row(
                    [
                        dbc.Col(tier_div),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(rarity_div),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(availability_div),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [dbc.Button(
                                    "Reload Table", 
                                    id="food-recipes-button",
                                    color="info")],
                                style = {"textAlign": "center"}
                            )
                        )
                    ]
                ),
            ],
            className="div-for-sidebar",
            width={"size": 12},
        )
    ],
    className="sidepanel",
)

