import dash
from dash import dash_table

from bs4 import BeautifulSoup
from markdown import *
import re

def markdown_to_text(markdown_string):
    """
    Converts a markdown string to plaintext
    Source: https://gist.github.com/lorey/eb15a7f3338f959a78cc3661fbc255fe
    """
    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown(markdown_string)

    # remove code snippets
    html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
    html = re.sub(r'<code>(.*?)</code >', ' ', html)

    # extract text
    soup = BeautifulSoup(html, "html.parser")
    text = ''.join(soup.findAll(text=True))

    return text

def get_food_recipes_table(df):
    return dash_table.DataTable(
        columns=[
            {"name": "Food Recipe", "id": "Food Recipe", "type": "text", 
             "presentation": "markdown"},
            {"name": "Difficulty", "id": "Difficulty", "type": "numeric"},
            {"name": "Tier", "id": "Tier", "type": "numeric"},
            {"name": "Rarity", "id": "Rarity", "type": "text"},
            {"name": "Availability", "id": "Availability", "type": "text"},
            {"name": "Base Price", "id": "Base Price", "type": "numeric"},
            {"name": "Base Time", "id": "Base Time", "type": "numeric"},
            {"name": "Base Ratio", "id": "Base Ratio", "type": "numeric"}
        ],
        data=df.to_dict('records'),
        page_size= 10,
        sort_action="native",
        sort_mode="multi",
        # Disable highlighting of active cell
        style_data_conditional=[    
            {
                "if": {"state": "selected"},
                "backgroundColor": "inherit !important",
                "border": "inherit !important",
            }  
        ],
        style_cell_conditional=[
            {
                'if': {
                    'column_type': 'text'
                },
                'textAlign': 'left'
            },
            {
                'if': {
                    'column_type': 'numeric'
                 },
                'textAlign': 'center'
            },            
        ],
        style_data={
            'color': 'black',
            'backgroundColor': 'white',
            'font-family': 'Noto Sans'
        },
        style_header={
            'backgroundColor': 'rgb(220, 220, 220)',
            'color': 'black',
            'font-family': 'Noto Sans',
            'fontWeight': 'bold',
            'textAlign': 'center'
        }
    )

def get_weapons_table(df):
    return dash_table.DataTable(
        columns=[
            {"name": "Weapon", "id": "Weapon", "type": "text", 
             "presentation": "markdown"},
            {"name": "Type", "id": "Type", "type": "text"},
            {"name": "Difficulty", "id": "Difficulty", "type": "numeric"},
            {"name": "Tier", "id": "Tier", "type": "numeric"},
            {"name": "Rarity", "id": "Rarity", "type": "text"},
            {"name": "Availability", "id": "Availability", "type": "text"},
            {"name": "Base Damage", "id": "Base Damage", "type": "numeric"},
            {"name": "Base Consumption", "id": "Base Consumption", "type": "numeric"},
        ],
        data=df.to_dict('records'),
        page_size= 10,
        sort_action="native",
        sort_mode="multi",
        # Disable highlighting of active cell
        style_data_conditional=[    
            {
                "if": {"state": "selected"},
                "backgroundColor": "inherit !important",
                "border": "inherit !important",
            }  
        ],
        style_cell_conditional=[
            {
                'if': {
                    'column_type': 'text'
                },
                'textAlign': 'left'
            },
            {
                'if': {
                    'column_type': 'numeric'
                 },
                'textAlign': 'center'
            },            
        ],
        style_data={
            'color': 'black',
            'backgroundColor': "white",
            'font-family': 'Noto Sans'
        },
        style_header={
            'backgroundColor': 'rgb(220, 220, 220)',
            'color': 'black',
            'font-family': 'Noto Sans',
            'fontWeight': 'bold',
            'textAlign': 'center'
        }
    )

