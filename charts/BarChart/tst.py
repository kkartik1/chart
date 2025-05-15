from vega_datasets import data
import BarChart as r
source = data.wheat()

#Simple Bar Chart
b = r.bar_chart(data=source, x='year', y='wheat', aln='V', srtf = 'wheat', srto = 'ascending', clr='wheat', tip=['wheat', 'year'], siz = 'X', txt='Example', leg= 'Y')
bar = b.create_chart()

source = data.barley()

#Grouped Bar Chart
b = r.bar_group(data=source, x='year', y='sum(yield)', z='site', aln='V', srtf = 'sum(yield)', srto = 'ascending', clr='year', tip=['site', 'year'], siz = 'X', txt='Example', leg= 'Y')
bar = b.create_chart()

#Stacked Bar Chart
b = r.bar_chart(data=source, x='variety', y='sum(yield)', aln='V', srtf = 'sum(yield)', srto = 'ascending', clr='site', tip=['variety', 'site'], siz = 'X', txt='Example', leg= 'Y')
bar = b.create_chart()