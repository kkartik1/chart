from vega_datasets import data
from ScatterPlot import chart as r
source = data.wheat()

#Scatter Bar Chart
b = r.scatter_chart(data=source, x='wheat', y='wages', clr='year', tip=['wheat','wages', 'year'], siz = 'X', hdg='Example', leg= 'Y')
bar = b.create_chart()

#Bubble Chart
b = r.bubble_chart(data=source, x='wheat', y='wages', siz1 = 'wages', clr='year', tip=['wheat','wages', 'year'], siz = 'X', hdg='Example')
bar = b.create_chart()