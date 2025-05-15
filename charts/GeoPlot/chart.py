import altair as alt
from vega_datasets import data
#base chart populated with X axis, Y axis, sort order and alignment (Vertical or Horizontal)
#Data, X axis variable & Y axis variable are compulsary fields
class base:
    #Initialize class variables 
    def __init__(self, data, tp, x):
        self.data = data
        self.tp = tp
        self.x = x
    #test code to check values in the class
    def __str__(self):
        #return f"{self.data[self.y]}"
        return f"{self.data.columns}"
    #Create base chart as per input provided  
    def create_base(self):
        if self.tp == 's':
            choro = 'states'
        else:
            choro = 'counties'
        usgeo = alt.topo_feature(data.us_10m.url, choro)
        base = alt.Chart(usgeo)
        return base
    
#Bar Chart inherits from the base class with additional features like color, tooltip, legend, text and heading  
#Simple bar chart and stacked bar chart could be created     
class us_choropleths(base):
    #Initialize class variables 
    def __init__(self, data, tp, x, clr=None, tip= None, leg= None, siz='M', txt=None, hdg=None):
        super().__init__(data, tp, x)
        self.clr = clr
        self.leg = leg
        self.tip = tip
        self.siz = siz
        self.txt = txt
        self.hdg = hdg
    #test code to check values in the class
    def __str__(self):
        #return f"{self.data[self.y]}"
        return f"{self.data.columns}"  
    #create bar chart as per input provided
    def create_chart(self):
        if self.siz == 'S':
            h = 75
            w = 200
        elif self.siz == 'M':
            h = 150
            w = 400
        elif self.siz == 'L':
            h = 250
            w = 600
        elif self.siz == 'X':
            h = 300
            w = 800
        if self.hdg == None:
            hd = ''
        else:
            hd = self.hdg
        tp = []
        if self.tip == None:
            tp = []
        else:
            for i in self.tip:
                tp.append(alt.Tooltip(f'{i}:N', title=f'{i}'))
        if self.clr == None:
            cl = ''
        else:
            if self.leg == None:
                cl = alt.Color(self.clr, legend=None)
            else:
                cl = alt.Color(self.clr, legend=alt.Legend(title=self.clr))
        base = super().create_base()
        if self.clr == None:
            if self.tip == None:
                choro = base.mark_geoshape().encode()
            else:
                choro = base.mark_geoshape().encode(tooltip=tp)
        else:
            if self.tip == None:
                choro = base.mark_geoshape().encode(color=cl)
            else:
                choro = base.mark_geoshape().encode(tooltip=tp, color=cl)
        if self.txt != None:
            txt = base.mark_text(
                        align='left',
                        baseline='middle',
                        dx=3  # Nudges text to right so it doesn't appear on top of the bar
                        ).encode(
                            text=self.txt
                        )
            choro = (choro+txt)
        chart = choro.transform_lookup(lookup='id',
                                       from_=alt.LookupData(self.data, self.x, self.data.columns.to_list())
                                       ).properties(height=h,width=w,
                                      title = alt.TitleParams(text = hd, 
                                                font = 'Arial', 
                                                fontSize = 20, 
                                                color = 'grey', 
                                                )
                                      ).project(type='albersUsa')
        return chart
        
