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

df = pd.read_csv("data/equipment_items.csv")

layout = html.Div([
    dcc.Loading(
        [
            html.Div(
                [functions.get_equipment_items_table(df)], 
                id="equipment-items-table")
        ]
    )
])