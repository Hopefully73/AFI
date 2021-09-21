import os

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

import numpy as np
import math
import time
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Alien Food Invasion Help"

server = app.server
app.config.suppress_callback_exceptions = True

armament_div = html.Div(
    [
        html.Div(
            [
                html.Img(src="./assets/img/Armament.jpg"),
            ],
            style={'textAlign': 'center'},
        ),
        html.H6(""),
        html.Br(),
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
            ]
        )
    ]
)

storage_div = html.Div(
    [
        html.Div(
            [
                html.Img(src="./assets/img/Storage.jpg"),
            ],
            style={'textAlign': 'center'},
        ),
        html.H6(""),
        html.Br(),
        dcc.Markdown("""
        The storage determines the maximum number of alien ingredients that can be collected.
        """),
        html.Br(),
        dbc.Row(
            [
               dbc.Col(
                    [
                        html.H6("Current Level"),
                        dcc.Input(
                            id="storage-current-level",
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
                        100 storage bins
                        """, id = "storage-current-value")
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
        html.H6(""),
        html.Br(),
        dcc.Markdown("""
        The motorization determines how long your drone can hunt aliens.
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
            ]
        )
    ]
)
    
inputs_div = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Img(src="./assets/img/question_mark.png", id = "storage-q",
                                 className = "question-ping"),
                        dbc.Tooltip(
                            children=[
                                """If yes, the algorithm ignores the storage as a potential next 
                                improvement and determines whether you should improve armament or 
                                motorization next."""],
                            target="storage-q",
                        ),
                        html.H6("Ignore Storage?"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": True},
                                {"label": "No", "value": False},
                            ],
                            value=False,
                            id="ignore-storage",
                            inline=True,
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.Img(src="./assets/img/question_mark.png", id = "motorization-q",
                                 className = "question-ping"),
                        dbc.Tooltip(
                            children=[
                                """If yes, the algorithm ignores the motorization as a potential 
                                next improvement and determines whether you should improve armament 
                                or storage next."""],
                            target="motorization-q",
                        ),
                        html.H6("Ignore Motorization?"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": True},
                                {"label": "No", "value": False},
                            ],
                            value=False,
                            id="ignore-motorization",
                            inline=True,
                        ), 
                    ]
                )
            ]
        ),
        html.Br(),
        html.Div(
            [
                dbc.Button(
                    ["Determine next drone part to improve"],
                    id="dbc-btn-improve",
                    color="info",
                    style={"font-size": 12,}
                ),
                html.H6(""),
                html.H4(
                    [
                        dcc.Loading(
                            "Press the button to get your first result!", 
                            id = "result"
                        ),
                    ],
                    id = "result-2",
                )
            ],
            style={"textAlign": "center"}
        ),
        
    ]
)

app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [armament_div], width={"size": 3},
                    className="div-for-headers",
                ),
                 dbc.Col(
                    [storage_div], width={"size": 3},
                    className="div-for-headers",
                ),
                 dbc.Col(
                    [motorization_div], width={"size": 3},
                    className="div-for-headers",
                ),
            ]
        ),
        dbc.Col(
            [inputs_div], width={"size": 4},
            className="div-for-headers-2",
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
    
# Callback for the storage current value
@app.callback(
    [
        Output("storage-current-value", "children"),
        Output("storage-current-value", "style"),
    ],
    Input("storage-current-level", "value"),
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
        x = 100 + (25 * (level - 1))
        return [f"{x} storage bins", None]
    
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

# Callback for getting the next drone part to improve
@app.callback(
    [
        Output("result", "children"),
        Output("result-2", "style"),
    ],
    Input("dbc-btn-improve", "n_clicks"),
    [
        State("armament-current-level", "value"),
        State("storage-current-level", "value"),
        State("motorization-current-level", "value"),
        State("ignore-storage", "value"),
        State("ignore-motorization", "value"),
    ],
)
def get_next_improve(n_clicks, armament, storage, motorization, ignore1, ignore2):
    if n_clicks:
        time.sleep(1) # To make the loading spinner visible
        inputs = {
            "Armament": armament,
            "Storage": storage,
            "Motorization": motorization,
        }
        if None in list(inputs.values()):
            missing_inputs = [x for x in list(inputs.keys()) if inputs[x] is None]
            error_message = f"Missing inputs: {', '.join(missing_inputs)}"
            return [error_message, {"color": "red"}]
        
        if (len(list(filter(lambda x: (isinstance(x, int)), 
                            [armament, storage, motorization]))) < 3):
            return [
                "All inputs need to be positive integers.", 
                {"color": "red"}
            ]
        
        # Current values for the three drone parts
        currentArmament = 20 + (4 * (armament - 1))
        currentStorage = 100 + (25 * (storage - 1))
        currentMotorization = 2 + (0.25 * (motorization - 1))
        
        # Current corresponding alien tech cost for the three drone parts
        def getCost(level):
            if level <= 30:
                costList = np.array([1, 2, 3, 5, 7, 10, 13, 16, 19, 22, 
                                     26, 30, 35, 40, 46, 52, 59, 66, 73, 80, 
                                     88, 96, 105, 114, 124, 136, 150, 164, 182, 200])
                currentCost = costList[level - 1]
            else:
                currentCost = 200 + (20 * (level - 30))
            return(currentCost)

        currentArmamentCost = getCost(armament)
        currentStorageCost = getCost(storage)
        currentMotorizationCost = getCost(motorization)
        
        # Other relevant values  
        nextArmament = currentArmament + 4
        nextMotorization = currentMotorization + 0.25
        storageUsed1 = nextArmament * currentMotorization
        storageUsed2 = currentArmament * nextMotorization
        
        # Corresponding decision trees for each situation
        if not ignore1 and  not ignore2:
            if storageUsed1 > currentStorage and storageUsed2 > currentStorage:
                return ["STORAGE", None]
            elif storageUsed1 > storageUsed2:
                return ["ARMAMENT", None]
            elif storageUsed1 < storageUsed2:
                return ["MOTORIZATION", None]
            else:
                if currentArmamentCost > currentMotorizationCost:
                    return ["MOTORIZATION", None]
                else:
                    return ["ARMAMENT", None]
        elif ignore1 and not ignore2:
            if storageUsed1 > storageUsed2:
                return ["ARMAMENT", None]
            elif storageUsed1 < storageUsed2:
                return ["MOTORIZATION", None]
            else:
                if currentArmamentCost > currentMotorizationCost:
                    return ["MOTORIZATION", None]
                else:
                    return ["ARMAMENT", None]   
        elif not ignore1 and ignore2:
            if storageUsed1 < currentStorage:
                return ["ARMAMENT", None]
            elif storageUsed1 > currentStorage:
                return ["STORAGE", None]
            else:
                if currentArmamentCost > currentStorageCost:
                    return ["STORAGE", None] 
                else:
                    return ["ARMAMENT", None]
        else:
            return ["ARMAMENT", None]
            
    else:
        raise PreventUpdate
    
if __name__ == '__main__':
    app.run_server()
    #app.run_server(debug=True)
