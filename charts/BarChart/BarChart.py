import altair as alt
#base chart populated with X axis, Y axis, sort order and alignment (Vertical or Horizontal)
#Data, X axis variable & Y axis variable are compulsary fields
class base:
    #Initialize class variables 
    def __init__(self, data, x, y, srtf= None, srto= None,  aln = 'H'):
        self.data = data
        self.x = x
        self.y = y
        self.srtf = srtf
        self.srto = srto
        self.aln = aln
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
        if self.aln == 'H':
            base = alt.Chart(self.data).encode(
                x=alt.X(self.x, type='ordinal', axis=alt.Axis(title=self.x), sort=srt),
                y=alt.Y(self.y, type='quantitative', axis=alt.Axis(title=self.y), stack='zero')
                )
        else:
            base = alt.Chart(self.data).encode(
                x=alt.X(self.y, type='quantitative', axis=alt.Axis(title=self.y), stack='zero'),
                y=alt.Y(self.x, type='ordinal', axis=alt.Axis(title=self.x), sort=srt)
                )
        return base
    
#Bar Chart inherits from the base class with additional features like color, tooltip, legend, text and heading  
#Simple bar chart and stacked bar chart could be created     
class bar_chart(base):
    #Initialize class variables 
    def __init__(self, data, x, y, srtf= None, srto= None, aln = 'H', clr=None, tip= None, leg= None, siz='M', txt=None, hdg=None):
        super().__init__(data, x, y, srtf, srto,  aln)
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
            
        if self.aln != 'H':
            z = h
            h = w
            w = z
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
                bar = base.mark_bar().encode()
            else:
                bar = base.mark_bar().encode(tooltip=tp)
        else:
            if self.tip == None:
                bar = base.mark_bar().encode(color=cl)
            else:
                bar = base.mark_bar().encode(tooltip=tp, color=cl)
        if self.txt != None:
            txt = bar.mark_text(
                        align='left',
                        baseline='middle',
                        dx=3  # Nudges text to right so it doesn't appear on top of the bar
                        ).encode(
                            text=self.txt
                        )
            bar = (bar+txt)
        chart = bar.properties(height=h,width=w,
                                      title = alt.TitleParams(text = hd, 
                                                font = 'Arial', 
                                                fontSize = 20, 
                                                color = 'grey', 
                                                )
                                      )
        return chart

#Inherits from the base calss and used for grouped bar chart
#Accepts one additional parameter z 
class bar_group(base):
    def __init__(self, data, x, y, z, srtf= None, srto= None, aln = 'H', clr=None, tip= None, leg= None, siz='M', txt=None, hdg=None):
        super().__init__(data, x, y, srtf, srto,  aln)
        self.z = z
        self.clr = clr
        self.leg = leg
        self.tip = tip
        self.siz = siz
        self.txt = None
        self.hdg = hdg
    def __str__(self):
        #return f"{self.data[self.y]}"
        return f"{self.data.columns}"    
    def create_chart(self):
        if self.siz == 'S':
            h = 75
            w = 30
        elif self.siz == 'M':
            h = 150
            w = 40
        elif self.siz == 'L':
            h = 250
            w = 50
        elif self.siz == 'X':
            h = 300
            w = 60
            
        if self.aln != 'H':
            z = h
            h = w
            w = z
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
        if self.aln == 'H':
            if self.clr == None:
                if self.tip == None:
                    bar = base.mark_bar().encode(column=self.z)
                else:
                    bar = base.mark_bar().encode(tooltip=tp, column=self.z)
            else:
                if self.tip == None:
                    bar = base.mark_bar().encode(color=cl, column=self.z)
                else:
                    bar = base.mark_bar().encode(tooltip=tp, color=cl, column=self.z)
        else:
            if self.clr == None:
                if self.tip == None:
                    bar = base.mark_bar().encode(row=self.z)
                else:
                    bar = base.mark_bar().encode(tooltip=tp, row=self.z)
            else:
                if self.tip == None:
                    bar = base.mark_bar().encode(color=cl, row=self.z)
                else:
                    bar = base.mark_bar().encode(tooltip=tp, color=cl, row=self.z)
        chart = bar.properties(height=h,width=w,
                                      title = alt.TitleParams(text = hd, 
                                                font = 'Arial', 
                                                fontSize = 20, 
                                                color = 'grey', 
                                                )
                                      )
        return chart
        
