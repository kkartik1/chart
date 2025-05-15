import altair as alt
import requests
import pandas as pd
import geopandas as gpd
import json


def download_json():
    '''Downloads ANC JSON from Open Data DC'''
    url = "https://opendata.arcgis.com/datasets/bfe6977cfd574c2b894cd67cf6a787c3_2.geojson"
    resp = requests.get(url)
    return resp.json()

def gen_base(geojson):
    '''Generates baselayer of DC ANC map'''
    base = alt.Chart(alt.Data(values=geojson)).mark_geoshape(
        stroke='black',
        strokeWidth=1
    ).encode(
    ).properties(
        width=400,
        height=400
    )
    return base

anc_json = download_json()
base_layer = gen_base(geojson=anc_json)
base_layer

gdf = gpd.GeoDataFrame.from_features((anc_json))
gdf.head()


pop_df = pd.read_csv('GeoPlot/anc_population.csv')
gdf = gdf.merge(pop_df, on='ANC_ID', how='inner')
gdf.head()

gdf['centroid_lon'] = gdf['geometry'].centroid.x
gdf['centroid_lat'] = gdf['geometry'].centroid.y
gdf.head()

choro_json = json.loads(gdf.to_json())
choro_data = alt.Data(values=choro_json['features'])


def gen_map(geodata, color_column, title):
    '''Generates DC ANC map with population choropleth and ANC labels'''
    # Add Base Layer
    base = alt.Chart(geodata, title = title).mark_geoshape(
        stroke='black',
        strokeWidth=1
    ).encode(
    ).properties(
        width=400,
        height=400
    )
    # Add Choropleth Layer
    choro = alt.Chart(geodata).mark_geoshape(
        fill='lightgray',
        stroke='black'
    ).encode(
        alt.Color(color_column, 
                  type='quantitative', 
                  scale=alt.Scale(scheme='bluegreen'),
                  title = "DC Population")
    )
    # Add Labels Layer
    labels = alt.Chart(geodata).mark_text(baseline='top'
     ).properties(
        width=400,
        height=400
     ).encode(
         longitude='properties.centroid_lon:Q',
         latitude='properties.centroid_lat:Q',
         text='properties.ANC_ID:O',
         size=alt.value(8),
         opacity=alt.value(1)
     )

    return base + choro + labels

pop_2000_map = gen_map(geodata=choro_data, color_column='properties.pop_2000', title='2000')


from vega_datasets import data
pop = data.population_engineers_hurricanes()
states = alt.topo_feature(data.us_10m.url, 'states')

variable_list = ['population', 'engineers', 'hurricanes']

x = alt.Chart(states).mark_geoshape().encode(
    color='population:Q'
).transform_lookup(
    lookup='id',
    from_=alt.LookupData(pop, 'id', list(pop.columns))
).properties(
    width=500,
    height=300
).project(
    type='albersUsa'
)
    
    
from vega_datasets import data
airports = data.airports()
airports.head()

x = alt.Chart(airports).mark_circle().encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    size=alt.value(10),
    tooltip='name'
).project(
    "albersUsa"
).properties(
    width=500,
    height=400
)
    
    
    
import altair as alt
import geopandas as gpd
import pandas as pd
import altair_viewer

path = "data/small_few_umbrella_terms_crimes_2021.csv"
df = pd.read_csv(path,encoding="utf_8",index_col='Unnamed: 0')

geometry = gpd.read_file("data_with_geo/geometry.geojson")


map_chart = alt.Chart(df).transform_lookup(
    lookup='label_dk',
    from_=alt.LookupData(geometry, 'label_dk',['geometry','type'])
).transform_aggregate(
    crime='sum(Anmeldte forbrydelser)',
    groupby=["label_dk","type","geometry"]
).mark_geoshape(
).encode(
    color=alt.Color(
        "crime:Q",
        scale=alt.Scale(
            scheme='viridis')
    )
)

altair_viewer.show(map_chart)