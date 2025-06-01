import geopandas as gpd
import base64
import io
import hashlib

def read_geojson(contents):
    try:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        gdf = gpd.read_file(io.BytesIO(decoded))
        return gdf, None
    except Exception as e:
        return None, str(e)

def detect_duplicates(gdf):
    gdf['geom_hash'] = gdf.geometry.apply(lambda geom: hashlib.md5(geom.wkb).hexdigest())
    return gdf[gdf.duplicated('geom_hash', keep=False)]

def detect_invalid_geometries(gdf):
    return gdf[~gdf.is_valid]
