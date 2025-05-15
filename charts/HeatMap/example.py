from vega_datasets import data
from HeatMap import chart as r
source = data.barley()

#Scatter Bar Chart
b = r.heat_map(data=source, x='variety', y='year', clr='sum(yield)', tip=['yield','variety', 'year'], siz = 'X', hdg='Example', leg= 'Y')
bar = b.create_chart()
