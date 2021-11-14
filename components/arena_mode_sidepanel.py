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

df = pd.read_csv("data/arena_mode.csv")

type_div = html.Div(
    [
        html.H6("Select mission type"),
        dbc.Checklist(
            options=[
                {"label": "Loot meat", "value": "Loot meat"},
                {"label": "Loot reptiloids and eggs", "value": "Loot reptiloids and eggs"},
                {"label": "Loot veggies", "value": "Loot veggies"},
                {"label": "Destroy container", "value": "Destroy container"},
            ],
            value=["Loot meat", "Loot reptiloids and eggs", "Loot veggies", "Destroy container"],
            id="arena-mode-mission-checklist",
            inline=True,
            persistence=True,
            persistence_type="memory",
        ),
    ]
)

include_div = html.Div(
    [
        html.H6("Include normal missions?"),
        dbc.RadioItems(
            options=[
                {"label": "Yes", "value": "yes"},
                {"label": "No", "value": "no"}
            ],
            value="yes",
            id="arena-mode-include-radio",
            inline=True,
            persistence=True,
            persistence_type="memory",
        ),
    ]
)

layout = dbc.Container(
    [
        dbc.Col(
            [
                dbc.Row(
                    [
                        dbc.Col(type_div),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(include_div),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [dbc.Button(
                                    "Reload Table", 
                                    id="arena-mode-button",
                                    color="primary")],
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

