from dash import Input, Output, State, dcc, html, dash_table
import dash_leaflet as dl
import dash_leaflet.express as dlx
from app import app
from app.utils import read_geojson, detect_duplicates, detect_invalid_geometries

global_gdf = {}

@app.callback(
    Output('file-info', 'children'),
    Output('tab-content', 'children'),
    Input('upload-geojson', 'contents'),
    State('upload-geojson', 'filename'),
    State('tabs', 'active_tab')
)
def update_dashboard(contents, filename, active_tab):
    if contents is None:
        return "", html.Div("Upload a GeoJSON file to get started.")

    gdf, error = read_geojson(contents)
    if error:
        return f"Error: {error}", html.Div("Failed to load GeoJSON.")

    global_gdf['gdf'] = gdf

    if active_tab == 'table':
        return f"Loaded file: {filename}", dash_table.DataTable(
            data=gdf.drop(columns='geometry').to_dict('records'),
            columns=[{"name": col, "id": col} for col in gdf.drop(columns='geometry').columns],
            page_size=10,
            style_table={'overflowX': 'auto'}
        )

    elif active_tab == 'map':
        return f"Loaded file: {filename}", dl.Map([
            dl.TileLayer(),
            dl.GeoJSON(data=gdf.__geo_interface__)
        ], style={'width': '100%', 'height': '600px'})

    elif active_tab == 'issues':
        dups = detect_duplicates(gdf)
        invalids = detect_invalid_geometries(gdf)
        return f"Loaded file: {filename}", html.Div([
            html.H5("Duplicate Geometries Found"),
            html.Div(f"{len(dups)} duplicates detected."),
            dash_table.DataTable(
                data=dups.to_dict('records'),
                columns=[{"name": col, "id": col} for col in dups.columns if col != 'geometry'],
                page_size=5,
                style_table={'overflowX': 'auto'}
            ),
            html.H5("Invalid Geometries Found"),
            html.Div(f"{len(invalids)} invalid geometries."),
            dash_table.DataTable(
                data=invalids.to_dict('records'),
                columns=[{"name": col, "id": col} for col in invalids.columns if col != 'geometry'],
                page_size=5,
                style_table={'overflowX': 'auto'}
            )
        ])
