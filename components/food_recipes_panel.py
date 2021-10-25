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

from index import app, server
from components import functions

df = pd.read_csv("data/food_recipes.csv", sep = "_")

layout = html.Div([
    dcc.Loading(
        [
            html.Div(
                [functions.get_food_recipes_table(df)], 
                id="food-recipes-table")
        ]
    )
])

# Callback for updating the table
@app.callback(
    Output("food-recipes-table", "children"),
    Input("food-recipes-button", "n_clicks"),
    [
        State("food-recipe-dropdown", "value"),
        State("food-recipe-tier-checklist", "value"),
        State("food-recipe-rarity-checklist", "value"),
        State("food-recipe-availability-radio", "value")
    ]
)
def update_table(n_clicks, recipe, tier, rarity, availability):
    if n_clicks:
        time.sleep(1)
        
        if recipe is None:
            cond1 = df["Tier"].isin(tier)
            cond2 = df["Rarity"].isin(rarity)
       
            if availability == "free":
                cond3 = df["Availability"].str.contains("re", regex=False)
            elif availability == "paid":
                cond3 = df["Availability"].str.contains("crystals", regex=False)
            else:
                cond3 = df["Availability"].str.contains("r", regex=False)

            new_df = df[cond1 & cond2 & cond3]
            
        else:
            df["Names"] = df["Food Recipe"].apply(functions.markdown_to_text)
            x = df["Names"].isin(recipe)
            new_df = df.loc[x]
    
        if len(new_df) == 0:
            return dcc.Markdown(
                """Empty table. Consider changing your inputs.""",
                style={"color": "red", "font-size": 20}
            )
        else:
            return functions.get_food_recipes_table(new_df)
    else:
        raise PreventUpdate
                
            