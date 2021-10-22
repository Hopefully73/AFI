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

from index import app

# Current corresponding alien tech cost for the three drone parts
def getCost(level):
    if level <= 30:
        costList = np.array([1, 2, 3, 5, 7, 10, 13, 16, 19, 22, 
                             26, 30, 35, 40, 46, 52, 59, 66, 73, 80, 
                             88, 96, 105, 114, 124, 136, 150, 164, 182, 200])
        currentCost = costList[level - 1]
    else:
        currentCost = 200
        for i in range(level - 30):
            increase = 20 + (5 * i)
            currentCost = currentCost + increase
    return(currentCost)

armament_div = html.Div(
    [
        html.Div(
            [
                html.Img(src="./assets/img/Armament.jpg"),
            ],
            style={'textAlign': 'center'},
        ),
        html.H6(""), html.Br(),
        dcc.Markdown("""
        The armament determines how many alien ingredients your drone can capture per hour.
        """),
        html.Br(),
        dbc.Row(
            [
               dbc.Col(
                    [
                        html.H6("Current Level"),
                        dcc.Input(
                            id="armament-current-level",
                            type="number",
                            min=1,
                            value=1,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                        ),  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Current Value"),
                        dcc.Markdown("""
                        20 ingredients per hour
                        """, id = "armament-current-value")
                    ]
                ),
                dbc.Col(
                    [
                        html.H6("Improve Cost"),
                        dcc.Markdown("""
                        1 alien tech
                        """, id = "armament-current-cost")
                    ]
                ),
            ]
        )
    ]
)

motorization_div = html.Div(
    [
        html.Div(
            [
                html.Img(src="./assets/img/Motorization.jpg"),
            ],
            style={'textAlign': 'center'},
        ),
        html.H6(""), html.Br(),
        dcc.Markdown("""
        The motorization determines how long your drone can hunt aliens to obtain
        alien ingredients.
        """),
        html.Br(),
        dbc.Row(
            [
               dbc.Col(
                    [
                        html.H6("Current Level"),
                        dcc.Input(
                            id="motorization-current-level",
                            type="number",
                            min=1,
                            value=1,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                        ),  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Current Value"),
                        dcc.Markdown("""
                        2:00 hours
                        """, id = "motorization-current-value")
                    ]
                ),
                dbc.Col(
                    [
                        html.H6("Improve Cost"),
                        dcc.Markdown("""
                        1 alien tech
                        """, id = "motorization-current-cost")
                    ]
                ),
            ]
        )
    ]
)

sensor_div = html.Div(
    [
        html.Div(
            [
                html.Img(src="./assets/img/Storage.jpg"),
            ],
            style={'textAlign': 'center'},
        ),
        html.H6(""), html.Br(), 
        dcc.Markdown("""
        The sensor improves the quality of alien ingredients. You need 100%
        sensor power to find rare ingredients.
        """, id = "sensor-description"),
        html.Br(),
        dbc.Row(
            [
               dbc.Col(
                    [
                        html.H6("Current Level"),
                        dcc.Input(
                            id="sensor-current-level",
                            type="number",
                            min=1,
                            value=1,
                            style={
                                "width": "60%",
                                "height": "25px",
                                "lineHeight": "25px",
                                "textAlign": "center",
                            },
                        ),  
                    ]
                ), 
                dbc.Col(
                    [
                        html.H6("Current Value"),
                        dcc.Markdown("""
                        50% power
                        """, id = "sensor-current-value")
                    ]
                ),
                dbc.Col(
                    [
                        html.H6("Improve Cost"),
                        dcc.Markdown("""
                        1 alien tech
                        """, id = "sensor-current-cost")
                    ]
                ),
            ]
        )
    ]
)

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [armament_div], width={"size": 4},
                    className="div-for-headers",
                ),
                 dbc.Col(
                    [motorization_div], width={"size": 4},
                    className="div-for-headers",
                ),
                 dbc.Col(
                    [sensor_div], width={"size": 4},
                    className="div-for-headers",
                ),
            ]
        ),
    ]
)

# Callback for the armament current value
@app.callback(
    [
        Output("armament-current-value", "children"),
        Output("armament-current-value", "style"),
    ],
    Input("armament-current-level", "value"),
)
def update_value(level):
    if level is None:
        return ["Missing input", {"color": "red"}]
    elif not isinstance(level, int):
        return [
            "The input needs to be a positive integer.", 
            {"color": "red"}
        ]
    else:
        x = 20 + (4 * (level - 1))
        return [f"{x} ingredients per hour", None]
    
# Callback for the armament improvement cost
@app.callback(
    [
        Output("armament-current-cost", "children"),
        Output("armament-current-cost", "style"),
    ],
    Input("armament-current-level", "value"),
)
def update_value(level):
    if level is None:
        return ["Missing input", {"color": "red"}]
    elif not isinstance(level, int):
        return [
            "The input needs to be a positive integer.", 
            {"color": "red"}
        ]
    else:
        x = getCost(level)
        return [f"{x} alien tech", None]    
    
# Callback for the motorization current value
@app.callback(
    [
        Output("motorization-current-value", "children"),
        Output("motorization-current-value", "style"),
    ],
    Input("motorization-current-level", "value"),
)
def update_value(level):
    if level is None:
        return ["Missing input", {"color": "red"}]
    elif not isinstance(level, int):
        return [
            "The input needs to be a positive integer.", 
            {"color": "red"}
        ]
    else:
        x = 2 + (0.25 * (level - 1))
        dec, num = math.modf(x)
        if dec == 0:
            dec = "00"
        elif dec == 0.25:
            dec = 15
        elif dec == 0.5:
            dec = 30
        else:
            dec = 45
            
        return [f"{num: .0f}:{dec} hours", None]   
    
# Callback for the motorization improvement cost
@app.callback(
    [
        Output("motorization-current-cost", "children"),
        Output("motorization-current-cost", "style"),
    ],
    Input("motorization-current-level", "value"),
)
def update_value(level):
    if level is None:
        return ["Missing input", {"color": "red"}]
    elif not isinstance(level, int):
        return [
            "The input needs to be a positive integer.", 
            {"color": "red"}
        ]
    else:
        x = getCost(level)
        return [f"{x} alien tech", None]       

# Callback for the sensor current value
@app.callback(
    [
        Output("sensor-current-value", "children"),
        Output("sensor-current-value", "style"),
    ],
    Input("sensor-current-level", "value"),
)
def update_value(level):
    if level is None:
        return ["Missing input", {"color": "red"}]
    elif not isinstance(level, int):
        return [
            "The input needs to be a positive integer.", 
            {"color": "red"}
        ]
    else:
        x = 50 + (10 * (level - 1))
        return [f"{x}% power", None] 

# Callback for the sensor description
@app.callback(
    [
        Output("sensor-description", "children"),
        Output("sensor-description", "style"),
    ],
    Input("sensor-current-level", "value"),
)
def update_value(level):
    if level is None:
        return ["Missing input", {"color": "red"}]
    elif not isinstance(level, int):
        return [
            "The input needs to be a positive integer.", 
            {"color": "red"}
        ]
    else:
        if level in range(0, 6):
            return ["""The sensor improves the quality of alien loot. 
            You need 100% power to find rare ingredients.""", None]
        elif level in range(6, 11):
            return ["""The sensor improves the quality of alien loot.
            You need 150% power to find alien crystals.""", None]
        elif level in range(11, 16):
            return ["""The sensor improves the quality of alien loot.
            You need 200% power to find alien tech.""", None]
        else:
            return ["""The sensor improves the quality of alien loot.
            More rare ingredients, crystals, and alien tech await.""", None]
    
# Callback for the sensor improvement cost
@app.callback(
    [
        Output("sensor-current-cost", "children"),
        Output("sensor-current-cost", "style"),
    ],
    Input("sensor-current-level", "value"),
)
def update_value(level):
    if level is None:
        return ["Missing input", {"color": "red"}]
    elif not isinstance(level, int):
        return [
            "The input needs to be a positive integer.", 
            {"color": "red"}
        ]
    else:
        x = getCost(level)
        return [f"{x} alien tech", None]