import altair as alt

#base chart populated with theta, color 
class base:
    #Initialize class variables 
    def __init__(self, data, val, cat, leg=None):
        self.data = data
        self.val = val
        self.cat = cat
        self.leg = leg
    #test code to check values in the class
    def __str__(self):
        #return f"{self.data[self.y]}"
        return f"{self.data.columns}"
    #Create base chart as per input provided  
    def create_base(self):
        if self.leg == None:
            base = alt.Chart(self.data).encode(
                    theta=alt.Theta(field=self.val, type="quantitative"),
                    color=alt.Color(field=self.cat, type="nominal", legend=None),
                    )
        else:
            base = alt.Chart(self.data).encode(
                    theta=alt.Theta(field=self.val, type="quantitative"),
                    color=alt.Color(field=self.cat, type="nominal"),
                    )
        return base
    
#Pie Chart inherits from the base class with additional features like tooltip, legend, text and heading  
#Simple pie chart could be created     
class pie_chart(base):
    #Initialize class variables 
    def __init__(self, data, val, cat, leg= None, tip= None, siz='M', txt=None, hdg=None):
        super().__init__(data, cat, val, leg=None)
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
            r = 20
            R = 40
        elif self.siz == 'M':
            h = 150
            w = 400
            r = 40
            R = 75
        elif self.siz == 'L':
            h = 250
            w = 600
            r = 60
            R = 100
        elif self.siz == 'X':
            h = 300
            w = 800
            r = 100
            R = 150
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
        base = super().create_base()
        if self.tip != None:
            pie = base.mark_arc(outerRadius=R).encode(tooltip=tp)
        else:
            pie = base.mark_arc(outerRadius=R).encode()
        if self.txt == 'Y':
            txt = base.mark_text(radius=R+20, size=14
                        ).encode(
                            text=self.cat
                        )
            pie = (pie+txt)
        chart = pie.properties(height=h,width=w,
                                      title = alt.TitleParams(text = hd, 
                                                font = 'Arial', 
                                                fontSize = 20, 
                                                color = 'grey', 
                                                )
                                      )
        return chart

#Inherits from the base calss and used for donut chart
#Adds radius
class donut_chart(base):
    #Initialize class variables 
    def __init__(self, data, val, cat, leg= None, tip= None, siz='M', txt=None, hdg=None):
        super().__init__(data, cat, val, leg=None)
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
            h = 150
            w = 200
            r = 20
            R = 40
        elif self.siz == 'M':
            h = 250
            w = 400
            r = 40
            R = 75
        elif self.siz == 'L':
            h = 400
            w = 600
            r = 60
            R = 100
        elif self.siz == 'X':
            h = 500
            w = 800
            r = 100
            R = 150
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
        base = super().create_base()
        if self.tip != None:
            pie = base.mark_arc(outerRadius=R, innerRadius=r).encode(tooltip=tp)
        else:
            pie = base.mark_arc(outerRadius=R, innerRadius=r).encode()
        if self.txt == 'Y':
            txt = base.mark_text(radius=R+20, size=14
                        ).encode(
                            text=self.cat
                        )
            pie = (pie+txt)
        chart = pie.properties(height=h,width=w,
                                      title = alt.TitleParams(text = hd, 
                                                font = 'Arial', 
                                                fontSize = 20, 
                                                color = 'grey', 
                                                )
                                      )
        return chart
    
#Inherits from the base calss and used for radian chart
#Adds a radian parameter
class radial_chart(base):
    #Initialize class variables 
    def __init__(self, data, val, cat, leg= None, tip= None, siz='M', txt=None, hdg=None):
        super().__init__(data, cat, val, leg=None)
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
            h = 150
            w = 200
            r = 20
            R = 40
        elif self.siz == 'M':
            h = 250
            w = 400
            r = 40
            R = 60
        elif self.siz == 'L':
            h = 400
            w = 600
            r = 60
            R = 80
        elif self.siz == 'X':
            h = 500
            w = 800
            r = 80
            R = 100
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
        base = super().create_base()
        if self.tip != None:
            pie = base.mark_arc(outerRadius=R, innerRadius=r).encode(radius=alt.Radius(self.val, scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),tooltip=tp)
        else:
            pie = base.mark_arc(outerRadius=R, innerRadius=r).encode(radius=alt.Radius(self.val, scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)))
        if self.txt == 'Y':
            txt = base.mark_text(radiusOffset=10
                        ).encode(
                            text=self.cat
                        )
            pie = (pie+txt)
        chart = pie.properties(height=h,width=w,
                                      title = alt.TitleParams(text = hd, 
                                                font = 'Arial', 
                                                fontSize = 20, 
                                                color = 'grey', 
                                                )
                                      )
        return chart
