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
                x=alt.X(self.x, type='temporal', axis=alt.Axis(title=self.x), sort=srt),
                y=alt.Y(self.y, type='quantitative', axis=alt.Axis(title=self.y), stack='zero')
                )
        else:
            base = alt.Chart(self.data).encode(
                x=alt.X(self.y, type='temporal', axis=alt.Axis(title=self.y), stack='zero'),
                y=alt.Y(self.x, type='quantitative', axis=alt.Axis(title=self.x), sort=srt)
                )
        return base
    
#line Chart inherits from the base class with additional features like color, tooltip, legend, text and heading  
#Simple line chart     
class line_chart(base):
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
    #create line chart as per input provided
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
                line = base.mark_line().encode()
            else:
                line = base.mark_line().encode(tooltip=tp)
        else:
            if self.tip == None:
                line = base.mark_line().encode(color=cl)
            else:
                line = base.mark_line().encode(tooltip=tp, color=cl)
        if self.txt != None:
            txt = line.mark_text(
                        align='left',
                        baseline='middle',
                        dx=3  # Nudges text to right so it doesn't appear on top of the line
                        ).encode(
                            text=self.txt
                        )
            line = (line+txt)
        chart = line.properties(height=h,width=w,
                                      title = alt.TitleParams(text = hd, 
                                                font = 'Arial', 
                                                fontSize = 20, 
                                                #color = 'grey', 
                                                )
                                      )
        return chart
    
# Base + trail
class varing_line_chart(base):
    #Initialize class variables 
    def __init__(self, data, x, y, srtf= None, srto= None, aln = 'H', clr=None, lwd=None, tip= None, leg= None, siz='M', txt=None, hdg=None):
        super().__init__(data, x, y, srtf, srto,  aln)
        self.clr = clr
        self.leg = leg
        self.tip = tip
        self.siz = siz
        self.txt = txt
        self.hdg = hdg
        self.lwd = lwd
    #test code to check values in the class
    def __str__(self):
        #return f"{self.data[self.y]}"
        return f"{self.data.columns}"  
    #create trail chart as per input provided
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
           # z = h
            h = w
            w = h
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
        if self.lwd == None:
            lwdth = self.y
        else:
            lwdth = self.lwd

        base = super().create_base()

        if self.clr == None:
            if self.tip == None:
                trail = base.mark_trail().encode(size=lwdth).interactive()
            else:
                trail = base.mark_trail().encode(size=lwdth,tooltip=tp).interactive()
        else:
            if self.tip == None:
                trail = base.mark_trail().encode(size=lwdth,color=cl).interactive()
            else:
                trail = base.mark_trail().encode(size=lwdth,tooltip=tp, color=cl).interactive()
        
        if self.txt != None:
            txt = trail.mark_text(
                        align='left',
                        basetrail='middle',
                        dx=3  # Nudges text to right so it doesn't appear on top of the trail
                        ).encode(
                            text=self.txt,
                        )
            trail = (trail+txt)
        chart = trail.properties(height=h,width=w,
                                      title = alt.TitleParams(text = hd, 
                                                font = 'Arial', 
                                                fontSize = 20, 
                                                color = 'grey', 
                                                )
                                      ).interactive()
        return chart
