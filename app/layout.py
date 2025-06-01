from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.H1("Farm GeoJSON Dashboard", className="my-4"),

    dcc.Upload(
        id='upload-geojson',
        children=html.Div(['Drag and Drop or ', html.A('Select a GeoJSON File')]),
        style={
            'width': '100%',
            'height': '80px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'marginBottom': '20px'
        },
        multiple=False
    ),
    html.Div(id='file-info'),

    dbc.Tabs([
        dbc.Tab(label='Table View', tab_id='table'),
        dbc.Tab(label='Map View', tab_id='map'),
        dbc.Tab(label='Geometry Checks', tab_id='issues'),
    ], id='tabs', active_tab='table'),

    html.Div(id='tab-content', className='p-4')
])
