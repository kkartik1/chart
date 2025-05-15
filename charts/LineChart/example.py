from vega_datasets import data
import sys
sys.path.insert(0, 'C:/Users/kkartik1/Documents/PythonScripts/RightPay/Visualization')
from LineChart import chart as r
import altair as alt
alt.renderers.enable('html')


#Simple line Chart
source = data.wheat()
b = r.line_chart(data=source, x='year', y='wheat', aln='H', srtf = 'year', srto = 'ascending', tip=['wheat', 'year'], siz='X', txt='wheat:O',leg= 'Y')
line = b.create_chart()
line.show()


#Line Chart with varying Size
source = data.wheat()
b = r.varing_line_chart(data=source, x='year', y='wheat', lwd = 'wages', aln='H', srtf = 'year', srto = 'ascending',tip=['wheat', 'year'],siz='X')
line = b.create_chart()
line.show()

#Multiple Line Chart
source = data.stocks()
b = r.line_chart(data=source,x='date', y='price',tip=['symbol','price'],clr='symbol',siz = 'X',leg = 'symbol')
line = b.create_chart()
line.show() 

import altair as alt
#Multiple lyared Line Chart
##comment line 23 and run from line 20
base = alt.Chart(source)
rule = base.mark_rule().encode(y='average(price)',color='symbol',size=alt.value(2),tooltip='average(price)')

c = line + rule
c.show()