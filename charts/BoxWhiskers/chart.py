import altair as alt
import altair_catplot as altcat
#base chart populated with X axis, Y axis, sort order and alignment (Vertical or Horizontal)
#Data, X axis variable & Y axis variable are compulsary fields
class base:
    #Initialize class variables 
    def __init__(self, data, x, y, srtf= None, srto= None):
        self.data = data
        self.x = x
        self.y = y
        self.srtf = srtf
        self.srto = srto
    #test code to check values in the class
    def __str__(self):
        #return f"{self.data[self.y]}"
        return f"{self.data.columns}"
    #Create base chart as per input provided  
    def create_base(self):
        if ((self.srtf == None) or (self.srto == None)):
            srt = None
        else:
            srt = alt.SortField(field=self.srtf, order=self.srto)
        
        base = alt.Chart(self.data).encode(
            x=alt.X(self.x, type='ordinal', axis=alt.Axis(title=self.x), sort=srt),
            y=alt.Y(self.y, type='quantitative', axis=alt.Axis(title=self.y), stack='zero')
            )
        return base
    
#Bar Chart inherits from the base class with additional features like color, tooltip, legend, text and heading  
#Simple bar chart and stacked bar chart could be created     
class box_whisker_chart(base):
    #Initialize class variables 
    def __init__(self, data, x, y, srtf= None, srto= None, clr=None, tip= None, leg= None, siz='M', txt=None, hdg=None):
        super().__init__(data, x, y, srtf, srto)
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
            b = 20
        elif self.siz == 'M':
            h = 150
            w = 400
            b = 40
        elif self.siz == 'L':
            h = 250
            w = 600
            b = 75
        elif self.siz == 'X':
            h = 300
            w = 800
            b = 100
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
                box = base.mark_boxplot(size=b, extent=0.5).encode()
            else:
                box = base.mark_boxplot(size=b, extent=0.5).encode(tooltip=tp)
        else:
            if self.tip == None:
                box = base.mark_boxplot(size=b, extent=0.5).encode(color=cl)
            else:
                box = base.mark_boxplot(size=b, extent=0.5).encode(tooltip=tp, color=cl)
        if self.txt != None:
            txt = box.mark_text(
                        align='left',
                        baseline='middle',
                        dx=3  # Nudges text to right so it doesn't appear on top of the bar
                        ).encode(
                            text=self.txt
                        )
            box = (box+txt)
        chart = box.properties(height=h,width=w,
                                      title = alt.TitleParams(text = hd, 
                                                font = 'Arial', 
                                                fontSize = 20, 
                                                color = 'grey', 
                                                )
                                      )
        return chart

#Bar Chart inherits from the base class with additional features like color, tooltip, legend, text and heading  
#Simple bar chart and stacked bar chart could be created     
class box_whisker_group(base):
    #Initialize class variables 
    def __init__(self, data, x, y, col, srtf= None, srto= None, clr=None, tip= None, leg= None, siz='M', txt=None, hdg=None):
        super().__init__(data, x, y, srtf, srto)
        self.col = col
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
            h = 50
            w = 80
            b = 10 
        elif self.siz == 'M':
            h = 75
            w = 100
            b = 15
        elif self.siz == 'L':
            h = 90
            w = 150
            b = 25
        elif self.siz == 'X':
            h = 120
            w = 200
            b = 40
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
                box = base.mark_boxplot(size=b, extent=0.5).encode(column=alt.Column(self.col, header=alt.Header(orient='bottom')))
            else:
                box = base.mark_boxplot(size=b, extent=0.5).encode(column=alt.Column(self.col, header=alt.Header(orient='bottom')), tooltip=tp)
        else:
            if self.tip == None:
                box = base.mark_boxplot(size=b, extent=0.5).encode(column=alt.Column(self.col, header=alt.Header(orient='bottom')), color=cl)
            else:
                box = base.mark_boxplot(size=b, extent=0.5).encode(column=alt.Column(self.col, header=alt.Header(orient='bottom')), tooltip=tp, color=cl)
        if self.txt != None:
            txt = box.mark_text(
                        align='left',
                        baseline='middle',
                        dx=3  # Nudges text to right so it doesn't appear on top of the bar
                        ).encode(
                            text=self.txt
                        )
            box = (box+txt)
        chart = box.properties(height=h,width=w,
                                      title = alt.TitleParams(text = hd, 
                                                font = 'Arial', 
                                                fontSize = 20, 
                                                color = 'grey', 
                                                )
                                      )
        return chart

    
class box_whisker_jitter():
    #Initialize class variables 
    def __init__(self, data, x, y, srtf= None, srto= None, clr=None, tip= None, leg= None, siz='M', txt=None, hdg=None):
        self.data = data
        self.x = x
        self.y = y
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
        if self.clr == None:
            if self.tip == None:
                box = altcat.catplot(self.data, height=h, width=w, mark='point',
                                     box_mark=dict(strokeWidth=2, opacity=0.6),
                                     whisker_mark=dict(strokeWidth=2, opacity=0.9),
                                     encoding=dict(x=alt.X(self.x),
                                                   y=alt.Y(self.y,scale=alt.Scale(zero=False))),
                                     transform='jitterbox',
                                     jitter_width=0.5)
            else:
                box = altcat.catplot(self.data, height=h, width=w, mark='point',
                                     box_mark=dict(strokeWidth=2, opacity=0.6),
                                     whisker_mark=dict(strokeWidth=2, opacity=0.9),
                                     encoding=dict(x=alt.X(self.x),
                                                   y=alt.Y(self.y,scale=alt.Scale(zero=False)),
                                                   tooltip = tp),
                                     transform='jitterbox',
                                     jitter_width=0.5)
        else:
            if self.tip == None:
                box = altcat.catplot(self.data, height=h, width=w, mark='point',
                                     box_mark=dict(strokeWidth=2, opacity=0.6),
                                     whisker_mark=dict(strokeWidth=2, opacity=0.9),
                                     encoding=dict(x=alt.X(self.x),
                                                   y=alt.Y(self.y,scale=alt.Scale(zero=False)),
                                                   color=cl),
                                     transform='jitterbox',
                                     jitter_width=0.5)
            else:
                box = altcat.catplot(self.data, 
                                     height=h, 
                                     width=w, 
                                     mark='point',
                                     box_mark=dict(strokeWidth=2, opacity=0.6),
                                     whisker_mark=dict(strokeWidth=2, opacity=0.9),
                                     encoding=dict(x=alt.X(self.x),
                                                   y=alt.Y(self.y,scale=alt.Scale(zero=False)),
                                                   color=cl, 
                                                   tooltip=tp),
                                     transform='jitterbox',
                                     jitter_width=0.5)
        if self.txt != None:
            txt = box.mark_text(
                        align='left',
                        baseline='middle',
                        dx=3  # Nudges text to right so it doesn't appear on top of the bar
                        ).encode(
                            text=self.txt
                        )
            box = (box+txt)
        chart = box.properties(title = alt.TitleParams(text = hd, 
                                                font = 'Arial', 
                                                fontSize = 20, 
                                                color = 'grey', 
                                                )
                                      )
        return chart
