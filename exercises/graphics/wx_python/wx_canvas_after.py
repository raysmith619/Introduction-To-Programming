#wx_panel_after.py 01Jul2023  crs, from panel_after.py
#                   24Oct2022  crs
import wx
import math
import time
import random


class CanvasFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(CanvasFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        self.is_painting = False    # Allow painting

        self.top_light = "gray"
        self.middle_light = "gray"
        self.bottom_light = "gray"
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle("wxPython Traffic Lights")
        self.Centre()
        self.Refresh()
        self.Show()
        
    def OnPaint(self, e):
        if self.is_painting:
            return

        self.is_painting = True     #suppress  derivative paints
        self.OnPaint2()
        self.is_painting = False
        
    def OnPaint2(self):
        dc = wx.PaintDC(self)
        # Establish sizes
        pn_width = 300          # panel size
        pn_height = pn_width*3
        panel = wx.Panel(self, size=wx.Size(width=pn_width, height=pn_height))

                
        # Coordinates within drawing area
        x_min = int(pn_width*.05)
        x_max = int(pn_width*.95)
        x_range = (x_max-x_min)
        x_mid = int((x_min+x_max)/2)
        y_min = int(pn_height*.1)
        y_max = int(pn_height*.95)
        y_mid = int((y_min+y_max)/2)
        y_range = abs(y_max-y_min)

        # Add drawing area

                    
        # Add title text
        title_text = "Event timing - using after()"
        title_font = wx.Font(wx.FontInfo(20))
        dc = wx.PaintDC(self)
        pen = wx.Pen(wx.Colour("blue"), 2, wx.SOLID)
        dc.SetPen(pen)
        dc.SetFont(title_font)
        title_w, title_h = dc.GetTextExtent(title_text)
        title_pt = wx.Point(int(x_mid - title_w / 2), int(y_min-title_h))
        ###dc.DrawText(text=title_text, pt=title_pt)
        dc.DrawText(text=title_text,  x=title_pt.x, y=title_pt.y)


        # Lights layout
        time_green = 2000         # time for green milliseconds
        time_red = 1000         # time for red milliseconds
        time_yellow = int(time_red/3)   # time for yellow
        self.light_size = y_range*.33
        light_spacer = self.light_size*.05
        yt = y_min
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

    def set_light(self, light_pos, color):
        """ Set light to color
        :light_pos: light center
        :color: light color string
        """
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen(color, style=wx.SOLID))
        dc.SetBrush(wx.Brush(color, wx.SOLID))
        dc.DrawCircle(light_pos, self.light_size)
        
        
    def red_light(self):
        """ Configure lights for red light """
        self.set_light(self.top_light, "gray")
        self.set_light(self.middle_light, "gray")
        self.set_light(self.bottom_light, "red")
        wx.CallLater(self.red_light, time_red)
                    
    def yellow_light(self):
        """ Configure lights for yellow light """
        self.set_light(self.top_light, "gray")
        self.set_light(self.middle_light, "yellow")
        self.set_light(self.bottom_light, "gray")
        wx.CallLater(self.red_light, time_yellow)

    def green_light(self):
        """ Configure lights for red light """
        self.set_light(self.top_light, "gray")
        self.set_light(self.middle_light, "gray")
        self.set_light(self.bottom_light, "green")
        wx.CallLater(self.yellow_light, time_green)

app = wx.App()
tlt = CanvasFrame(None)

# Start the loop
tlt.Refresh()
        
app.MainLoop()
