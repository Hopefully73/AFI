import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash_table.Format import Format, Scheme, Group
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import math
import time
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from index import app, server
from components import functions

df = pd.read_csv("data/arena_mode.csv")

layout = html.Div([
    dcc.Loading(
        [
            html.Div(
                [functions.get_arena_mode_table(df)], 
                id="arena-mode-table")
        ]
    )
])

# Callback for updating the table
@app.callback(
    Output("arena-mode-table", "children"),
    Input("arena-mode-button", "n_clicks"),
    [
        State("arena-mode-mission-checklist", "value"),
        State("arena-mode-include-radio", "value")
    ]
)
def update_table(n_clicks, mission, include):
    if n_clicks:
        time.sleep(1)
        
        if include == "no":
            cond1 = df["Mission Type"].isin(mission)
            # All missions except for "None"
            cond2 = ~df["Mission Type"].str.contains("Normal", regex=False)
            new_df = df[cond1 & cond2]
        else:
            mission_values = mission.append("Normal")
            cond = df["Mission Type"].isin(mission)
            new_df = df[cond] 
        
        if len(new_df) == 0:
            return dcc.Markdown(
                """Empty table. Consider changing your inputs.""",
                style={"color": "red", "font-size": 20}
            )
        else:
            return functions.get_arena_mode_table(new_df)
    else:
        raise PreventUpdate
        
        