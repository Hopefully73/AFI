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

df = pd.read_csv("data/weapons.csv")

layout = html.Div([
    dcc.Loading(
        [
            html.Div(
                [functions.get_weapons_table(df)], 
                id="weapons-table")
        ]
    )
])

# Callback for updating the table
@app.callback(
    Output("weapons-table", "children"),
    Input("weapons-button", "n_clicks"),
    [
        State("weapon-dropdown", "value"),
        State("weapon-type-checklist", "value"),
        State("weapon-tier-checklist", "value"),
        State("weapon-rarity-checklist", "value"),
        State("weapon-availability-radio", "value")
    ]
)
def update_table(n_clicks, weapon, typ, tier, rarity, availability):
    if n_clicks:
        time.sleep(1)
        
        if weapon is None:
            cond1 = df["Type"].isin(typ)
            cond2 = df["Tier"].isin(tier)
            
            if len(rarity) == 0:
                return dcc.Markdown(
                    """Empty table. Consider changing your inputs.""",
                    style={"color": "red", "font-size": 20}
                )
            else:
                cond3 = df["Rarity"].astype(str).str.contains("|".join(rarity))
       
            if availability == "free":
                cond4 = df["Availability"].str.contains("re", regex=False)
            elif availability == "paid":
                cond4 = df["Availability"].str.contains("crystals", regex=False)
            else:
                cond4 = df["Availability"].str.contains("r", regex=False)

            new_df = df[cond1 & cond2 & cond3 & cond4]
        
        else:
            df["Names"] = df["Weapon"].apply(functions.markdown_to_text)
            x = df["Names"].isin(weapon)
            new_df = df.loc[x]
        
        if len(new_df) == 0:
            return dcc.Markdown(
                """Empty table. Consider changing your inputs.""",
                style={"color": "red", "font-size": 20}
            )
        else:
            return functions.get_weapons_table(new_df)
    else:
        raise PreventUpdate

        