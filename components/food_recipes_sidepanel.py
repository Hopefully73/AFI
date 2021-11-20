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

df = pd.read_csv("data/food_dishes.csv", sep = "_")
df["Names"] = df["Food Dish"].apply(functions.markdown_to_text)
x = df["Names"].unique()
x.sort()

search_recipe_div = html.Div(
    [
        html.H6("Search food dish"),
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

search_ing_div = html.Div(
    [
        html.H6("Search ingredient"),
        dcc.Dropdown(
            id="ingredient-dropdown",
            options=[
                {"label": "Alien claw", "value": "A. claw"},
                {"label": "Alien egg", "value": "A. egg"},
                {"label": "Alien egg goo", "value": "A. egg goo"},
                {"label": "Alien egg jelly", "value": "A. egg jelly"},
                {"label": "Alien meat", "value": "A. meat"},
                {"label": "Alien thigh", "value": "A. thigh"},
                {"label": "Alien tongue", "value": "A. tongue"},
                {"label": "Commander antennas", "value": "C. antennas"},
                {"label": "Commander brain", "value": "C. brain"},
                {"label": "Commander eye", "value": "C. eye"},
                {"label": "Commander heart", "value": "C. heart"},
                {"label": "Reptiloid claws", "value": "R. claws"},
                {"label": "Reptiloid fillet", "value": "R. fillet"},
                {"label": "Reptiloid fin", "value": "R. fin"},
                {"label": "Reptiloid tentacle", "value": "R. tentacle"},
                {"label": "Veggie alien blossom", "value": "V.A. blossom"},
                {"label": "Veggie alien bud", "value": "V.A. bud"},
                {"label": "Veggie alien fruit", "value": "V.A. fruit"},
                {"label": "Veggie alien grain spike", "value": "V.A. grain spike"},
                {"label": "Veggie alien root", "value": "V.A. root"},
                {"label": "Veggie alien seeds", "value": "V.A. seeds"},
                {"label": "Veggie alien sprout", "value": "V.A. sprout"},
            ],
            persistence=True,
            persistence_type="memory",
            placeholder = "Choose one from the list."
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
                {"label": "Merchant", "value": "paid"},
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
                        dbc.Col(search_recipe_div),
                    ]
                ),
                html.H6(""),
                dbc.Row(
                    [
                        dbc.Col(search_ing_div),
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

