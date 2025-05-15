from GeoPlot import chart as r
import pandas as pd

popdta = 'GeoPlot/uspopulation.xlsx'
pp = pd.read_excel(popdta, index_col=None)

#Simple Choropleth maps by County
b = r.us_choropleths(data=pp, tp = 'c', x='Id', clr='Data:Q', txt = 'Rank:N', tip=['Data', 'Rank', 'County'], siz = 'L', hdg='Example')
choro = b.create_chart()

geodta = 'GeoPlot/usstates.xlsx'
st = pd.read_excel(geodta, index_col=None)

stt = pd.DataFrame(st).groupby(['state_abr', 'state_name'],as_index=False).agg(
                id = pd.NamedAgg(column="state_id", aggfunc="max"))    

pop = pd.DataFrame(pp).groupby(['State'],as_index=False).agg(
                population = pd.NamedAgg(column="Data", aggfunc="sum"))

st_df = stt.rename(columns={'state_abr': 'State'})
df = pd.merge(st_df, pop, how="inner", on=["State"])

#Simple Choropleth maps by State
b = r.us_choropleths(data=df, tp = 's', x='id', clr='population:Q', txt = 'State:N', tip=['State', 'state_name', 'population'], siz = 'X', hdg='Example')
choro = b.create_chart()
