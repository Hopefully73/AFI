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

df = pd.read_csv("data/equipment_items.csv")

layout = dbc.Container(
    [
        dbc.Col(
            [
                html.H5(html.B("Definitions:")),
                html.Br(),
                html.H6(html.B("Availability")),
                html.H6("- total  no. of stars required to unlock the equipment item"),
                html.H6(html.B("Damage")),
                html.H6("- total normal attack damage from all family members' weapons"),
                html.H6(html.B("Use")),
                html.H6("""- no. of times this item can be used per mission; has a cooldown 
                        prior to every use"""),
                html.H6(html.B("A.T.")),
                html.H6("- alien tech"),
                html.H6(html.B("A.S. with R. or L.")),
                html.H6("- alien stuff; rare or legendary")
            ],
            className="div-for-sidebar",
            width={"size": 12},
        )
    ],
    className="sidepanel"
)