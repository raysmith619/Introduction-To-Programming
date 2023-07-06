#wx_canvas_after.py 01Jul2023  crs, from canvas_after.py
#                   24Oct2022  crs
"""
wxPython version of an event based display:
Two dimensional version of a traffic light
"""
import wx
import math
import time
import random

pn_width = 300
pn_height = int(pn_width*3)

class LightColorTimes:

    def __init__(self, state, color, duration):
        self.state = state
        self.color = color
        self.duration = duration
        
class CanvasFrame(wx.Frame):
    GREEN = 1
    YELLOW = 2
    RED = 3
    
    def __init__(self, *args, **kw):
        super(CanvasFrame, self).__init__(*args, **kw)
        """ light color, timing """
        time_green = 2000         # time for green milliseconds
        time_red = int(time_green/2)         # time for red milliseconds
        time_yellow = int(time_red/3)   # time for yellow

        color_red = wx.Colour(0xB81D13)
        color_green = wx.Colour(0x008450)
        color_yellow = wx.Colour(0xEFB700)
        self.lcolt = {} # state,color, time by state
        self.lcolt[self.RED] = LightColorTimes(self.RED, color_red, time_red)
        self.lcolt[self.YELLOW] = LightColorTimes(self.YELLOW, color_yellow, time_yellow)
        self.lcolt[self.GREEN] = LightColorTimes(self.GREEN, color_green, time_green)
        self.InitUI()

    def InitUI(self):
        
        self.is_painting = False    # Allow painting

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle("wxPython Traffic Lights")
        self.Centre()
        self.Refresh()
        self.Show()

    def Start(self, state=None):
        """ Start lighted sequence
        :state: state default: GREEN
        """
        if state is None:
            state = self.GREEN
            
        self.state = state
        wx.CallLater(0, self.loop_states)

    def loop_states(self):
        """ Loop over light states at appropriate timings
        """
        self.next_state()
        state = self.state
        ###print(f"loop_states: state{state}")
        wx.CallLater(0, self.Refresh)
        duration = self.lcolt[state].duration
        wx.CallLater(duration, self.loop_states)
            
                            
    def OnPaint(self, e):
        ###print(f"\nOnPaint {self.state}")
        if self.is_painting:
            return

        self.is_painting = True     #suppress  derivative paints
        self.OnPaint2()
        self.is_painting = False
        
    def OnPaint2(self):
        ###print(f"OnPaint2 {self.state}")
        rect = self.GetClientRect()
        x_min = rect.x
        x_max = x_min + rect.width
        y_min = rect.y
        y_max = y_min + rect.height
        dc = wx.PaintDC(self)
        # Establish sizes

                
        # Coordinates within drawing area
        #x_min = int(pn_width*.05)
        #x_max = int(pn_width*.95)
        x_range = (x_max-x_min)
        x_mid = int((x_min+x_max)/2)
        #y_min = int(pn_height*.05)
        #y_max = int(pn_height*.90)
        y_mid = int((y_min+y_max)/2)
        y_range = abs(y_max-y_min)

        # Add drawing area

                    
        # Add title text
        title_text = "wxPython Event timing\n - using CallLater()"
        title_font = wx.Font(wx.FontInfo(20))
        dc = wx.PaintDC(self)
        pen = wx.Pen(wx.Colour("blue"), 2, wx.SOLID)
        dc.SetPen(pen)
        dc.SetFont(title_font)
        title_w, title_h = dc.GetTextExtent(title_text)
        th = 2*title_h
        light_range = y_range - th
        title_pt = wx.Point(int(x_mid-title_w/4), int(y_min))
        ###dc.DrawText(text=title_text, pt=title_pt)
        dc.DrawText(text=title_text,  x=title_pt.x, y=title_pt.y)


        # Lights layout
        self.light_size = int(.95*light_range/3)
        light_spacer = int(self.light_size*.05)
        yt = y_min+th
        ytb = yt + self.light_size
        yt_c = int((yt+ytb)/2)
        self.top_light = wx.Point(x_mid,yt_c)
        
        ym = ytb + light_spacer
        ymb = ym + self.light_size
        ym_c = int((ym+ymb)/2)
        self.middle_light = wx.Point(x_mid,ym_c)
        
        yb = ymb + light_spacer
        ybb = yb + self.light_size
        yb_c = int((yb+ybb)/2)
        self.bottom_light = wx.Point(x_mid,yb_c)
        self.draw_lights()
        
    def draw_lights(self, state=None):
        """ Draw in given state
        :state: light state default: current state
        """
        if state is None:
            state = self.state
        if state == self.GREEN:
            self.green_light()
        elif state == self.YELLOW:
            self.yellow_light()
        else:
            self.red_light()
            
    def color_light(self, light_pos, color):
        """ Set light to color
        :light_pos: light center
        :color: light color string
        """
        print(f"color_light({light_pos}, {color})")
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen(color, style=wx.SOLID))
        dc.SetBrush(wx.Brush(color, wx.SOLID))
        dc.DrawCircle(light_pos, int(self.light_size/2))
        print()
    
    def next_state(self):
        """ Advance light state
        """
        if self.state == self.RED:
            self.state = self.GREEN
        elif self.state == self.GREEN:
            self.state = self.YELLOW
        elif self.state == self.YELLOW:
            self.state = self.RED
        else:
            print(f"Unexpected state {self.state}")
        ###print(f"next_state: {self.state}")    
        
    
    def set_light(self, state=None):
        """ Set light state
        """
        if state is None:
            state = self.RED
        self.state = state
        ###print(f"set_state: {self.state}")    
       
        
    def red_light(self):
        """ Configure lights for red light """
        self.state = self.RED
        #self.color_light(self.top_light, self.lcolt[self.RED].color)
        self.color_light(self.top_light, wx.Colour(184,29,19))
        self.color_light(self.middle_light, "gray")
        self.color_light(self.bottom_light, "gray")

                    
    def yellow_light(self):
        self.state =  self.YELLOW
        """ Configure lights for yellow light """
        self.color_light(self.top_light, "gray")
        #self.color_light(self.middle_light, self.lcolt[self.YELLOW].color)
        self.color_light(self.middle_light, wx.Colour(239,183,0))
        self.color_light(self.bottom_light, "gray")


    def green_light(self):
        self.state = self.GREEN
        """ Configure lights for green light """
        self.color_light(self.top_light, "gray")
        self.color_light(self.middle_light, "gray")
        self.color_light(self.bottom_light, self.lcolt[self.GREEN].color)


app = wx.App()
tlt = CanvasFrame(None, size=wx.Size(pn_width, pn_height))

# Start the loop
tlt.Start()
        
app.MainLoop()
