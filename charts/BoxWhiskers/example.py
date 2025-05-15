from vega_datasets import data
from BoxWhiskers import chart as r
source = data.cars()

#Simple Box Plot
b = r.box_whisker_chart(data=source, x='Origin', y='Horsepower', srtf = 'Origin', srto = 'descending', clr='Origin', tip=['Origin', 'Horsepower'], siz = 'L', hdg='Example')
box = b.create_chart()

#Jitter Box plot
b = r.box_whisker_jitter(data=source, x='Origin:N', y='Horsepower:Q', clr='Origin', tip=['Origin', 'Horsepower'], siz = 'L', hdg='Example')
box = b.create_chart()

#Grouped Box Chart
b = r.box_whisker_group(data=source, x='Cylinders', y='Horsepower', col='Origin', srtf = 'Origin', srto = 'descending', clr='Origin', tip=['Origin', 'Horsepower'], siz = 'X', hdg='Example')
box = b.create_chart()