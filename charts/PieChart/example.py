from PieChart import chart as r
from vega_datasets import data
import pandas as pd

source = pd.DataFrame(data.barley())
source1 = source.groupby(['site']).agg(
        {
         'yield':'sum',     
         }
        ).reset_index()
source1['yield']= source1['yield'].round()
#Pie Chart
b = r.pie_chart(source1, 'site', 'yield')
pie = b.create_chart()

#Donut Chart
b = r.donut_chart(data=source1, val='site', cat='yield', tip=['yield', 'site'], siz = 'L', hdg='Example', leg= 'Y', txt='Y')
pie = b.create_chart()

#Radial Chart
b = r.radial_chart(data=source1, val='site', cat='yield', tip=['yield', 'site'], siz = 'L', hdg='Example', leg= 'Y', txt='Y')
pie = b.create_chart()