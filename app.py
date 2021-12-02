import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc

import numpy as np
import math
import time
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from components import (
    food_recipes_sidepanel, food_recipes_panel,
    weapons_sidepanel, weapons_panel, 
    equipment_items_sidepanel, equipment_items_panel,
    arena_mode_sidepanel, arena_mode_panel,
    drone, header, functions
)

from index import app, server

tab1_panels = dbc.Container([food_recipes_panel.layout])
tab2_panels = dbc.Container([weapons_panel.layout])
tab3_panels = dbc.Container([equipment_items_panel.layout])
tab4_panels = dbc.Container([drone.layout])
tab5_panels = dbc.Container([arena_mode_panel.layout])

tabs_div = html.Div(
    [
        dcc.Tabs(
            id="tabs-with-classes",
            value="tab-1",
            parent_className="custom-tabs",
            className="custom-tabs-container",
            children=[
                dcc.Tab(
                    label="Food Dishes",
                    value="tab-1",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Weapons",
                    value="tab-2",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Equipment Items",
                    value="tab-3",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Drone",
                    value="tab-4",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Arena Mode",
                    value="tab-5",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
            ],
        ),
        html.Div(id="tabs-content-classes"),
    ],
)

app.layout = html.Div(
    [
        header.layout,
        dbc.Row(
            [
                dbc.Col(width={"size": 1}),
                dbc.Col(tabs_div),
            ],
            className="header_row",
        )
    ]
)


@app.callback(
    Output("tabs-content-classes", "children"),
    Input("tabs-with-classes", "value"),
)
def render_content(tab):
    if tab == "tab-2":
        return dbc.Row(
            [
                dbc.Col(
                    html.Div([weapons_sidepanel.layout]),
                    width={"size": 4},
                    className="sidepanel-sticky",
                ),
                dbc.Col(
                    html.Div([tab2_panels]),
                    width={"size": 8},
                    style={"padding-right": "5em"},
                    className="output-container",
                ),
            ]
        )
    elif tab == "tab-3":
        return dbc.Row(
            [
                dbc.Col(
                    html.Div([equipment_items_sidepanel.layout]),
                    width={"size": 3},
                    className="sidepanel-sticky",
                ),
                dbc.Col(
                    html.Div([tab3_panels]),
                    width={"size": 9},
                    style={"padding-right": "5em"},
                    className="output-container",
                ),
            ]
        )
    elif tab == "tab-4":
        return dbc.Row(
            [
                dbc.Col(
                    html.Div([tab4_panels]),
                    style={"padding-right": "5em"},
                    className="output-container",
                ),
            ]
        )
    elif tab == "tab-5":
        return dbc.Row(
            [
                dbc.Col(
                    html.Div([arena_mode_sidepanel.layout]),
                    width={"size": 4},
                    className="sidepanel-sticky",
                ),
                dbc.Col(
                    html.Div([tab5_panels]),
                    width={"size": 5},
                    style={"padding-right": "5em"},
                    className="output-container",
                ),
            ]
        )
    else:
        return dbc.Row(
            [
                dbc.Col(
                    html.Div([food_recipes_sidepanel.layout]),
                    width={"size": 3},
                    className="sidepanel-sticky",
                ),
                dbc.Col(
                    html.Div([tab1_panels]),
                    width={"size": 9},
                    style={"padding-right": "5em"},
                    className="output-container",
                ),
            ]
        )         
    
if __name__ == '__main__':
    app.run_server()
    #app.run_server(debug=True)
