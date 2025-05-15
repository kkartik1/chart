import altair as alt
#base chart populated with X axis, Y axis, sort order and alignment (Vertical or Horizontal)
#Data, X axis variable & Y axis variable are compulsary fields
class base:
    #Initialize class variables 
    def __init__(self, data, x, y):
        self.data = data
        self.x = x
        self.y = y
    #test code to check values in the class
    def __str__(self):
        #return f"{self.data[self.y]}"
        return f"{self.data.columns}"
    #Create base chart as per input provided  
    def create_base(self):
        base = alt.Chart(self.data).encode(
                x=alt.X(self.x, type='ordinal', axis=alt.Axis(title=self.x)),
                y=alt.Y(self.y, type='quantitative', axis=alt.Axis(title=self.y))
            )
        return base
    
#Bar Chart inherits from the base class with additional features like color, tooltip, legend, text and heading  
#Simple bar chart and stacked bar chart could be created     
class scatter_chart(base):
    #Initialize class variables 
    def __init__(self, data, x, y, clr=None, tip= None, leg= None, siz='M', txt=None, hdg=None):
        super().__init__(data, x, y)
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
            s = 40
        elif self.siz == 'M':
            h = 150
            w = 400
            s = 60
        elif self.siz == 'L':
            h = 250
            w = 600
            s = 80
        elif self.siz == 'X':
            h = 300
            w = 800
            s = 100
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
                bar = base.mark_circle(color='#000080',
                                       size=s,
                                       opacity=0.6,
                                       stroke='black',
                                       strokeWidth=0
                                       ).encode()
            else:
                bar = base.mark_circle(color='#000080',
                                       size=s,
                                       opacity=0.6,
                                       stroke='black',
                                       strokeWidth=0
                                       ).encode(tooltip=tp)
        else:
            if self.tip == None:
                bar = base.mark_circle(color='#000080',
                                       size=s,
                                       opacity=0.6,
                                       stroke='black',
                                       strokeWidth=0
                                       ).encode(color=cl)
            else:
                bar = base.mark_circle(color='#000080',
                                       size=s,
                                       opacity=0.6,
                                       stroke='black',
                                       strokeWidth=0
                                       ).encode(tooltip=tp, color=cl)
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
class bubble_chart(base):
    #Initialize class variables 
    def __init__(self, data, x, y, siz1=None, clr=None, tip= None, leg= None, siz='M', txt=None, hdg=None):
        super().__init__(data, x, y)
        self.clr = clr
        self.siz1 = siz1
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
            s = 40
        elif self.siz == 'M':
            h = 150
            w = 400
            s = 60
        elif self.siz == 'L':
            h = 250
            w = 600
            s = 80
        elif self.siz == 'X':
            h = 300
            w = 800
            s = 100
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
        if self.leg == None:
            sz = alt.Size(self.siz1, scale=alt.Scale(range=[0, 4000]), legend=None)
        else:
            sz = alt.Size(self.siz1, scale=alt.Scale(range=[0, 4000]), legend=alt.Legend(title=self.siz1))
        base = super().create_base()
        if self.clr == None:
            if self.tip == None:
                bar = base.mark_circle(color='#000080',
                                       size=s,
                                       opacity=0.6,
                                       stroke='black',
                                       strokeWidth=0
                                       ).encode(sz)
            else:
                bar = base.mark_circle(color='#000080',
                                       size=s,
                                       opacity=0.6,
                                       stroke='black',
                                       strokeWidth=0
                                       ).encode(sz,tooltip=tp)
        else:
            if self.tip == None:
                bar = base.mark_circle(color='#000080',
                                       size=s,
                                       opacity=0.6,
                                       stroke='black',
                                       strokeWidth=0
                                       ).encode(sz, color=cl)
            else:
                bar = base.mark_circle(color='#000080',
                                       size=s,
                                       opacity=0.6,
                                       stroke='black',
                                       strokeWidth=0
                                       ).encode(sz, tooltip=tp, color=cl)
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
        
