
#wx_canvas_lines.py 08Jun2023  crs, from canvas_lines.py

"""
wxPython version of tkinter Canvas lines examples
Note wxPython does not have a Canvas widget which exists in tkinter
Thanks to Jan Bodnar (zetcode.com) for his wxPython examples on which I've drawn

"""
from random import uniform
import wx

cv_width = 300
cv_height = cv_width*2
x_min = int(cv_width*.1)
x_max = int(cv_width*.9)
pat_width = x_max-x_min
x_mid = int((x_min+x_max)/2)
x_range = (x_max-x_min)

y_min = int(cv_height*.1)
y_max = int(cv_height*.9)
y_mid = int((y_min+y_max)/2)
pat_height = y_max-y_min
y_range = abs(y_max-y_min)

background = "very light gray"

# Connect random points
npts = 15
points = []    # List of wx.Point
for i in range(npts):
    x = uniform(x_min,x_max)
    y = uniform(y_min, y_max)
    point = wx.Point(int(x), int(y))
    points.append(point)


class CanvasFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(CanvasFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        self.SetBackgroundColour(wx.Colour(background))
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle("wxPython Canvas lines")
        self.Centre()

    def OnPaint(self, e):
        self.SetBackgroundColour(wx.Colour(background))
        dc = wx.PaintDC(self)
        thickness = 2
        pt_text_color = "blue"      # Number text label color
        pt_num_color = "blue"       # Number number label color
        pen = wx.Pen(wx.Colour("green"), thickness, wx.SOLID)
        dc.SetPen(pen)
        dc.DrawLines(points)

        # Mark points
        pt_strs = []        # Point label strings
        pt_coords = []      # Point string coordinates
        pt_fonts = []       # Point label fonts
        pt_colors = []      # Point colors
        pt_text_font = wx.Font(wx.FontInfo(18))
        pt_text_dc = wx.PaintDC(self)
        pt_num_font = wx.Font(wx.FontInfo(15))
        pt_num_dc = wx.PaintDC(self)
        for n in range(1, npts + 1):
            i = n - 1
            pt_color = "blue"

            if n == 1:
                pt_str = "Start"
                pt_color = pt_text_color
                pt_font = pt_text_font
                pt_str_w, pt_str_h = pt_text_dc.GetTextExtent(pt_str)
            elif n == npts:
                pt_str = "End"
                pt_color = pt_text_color
                pt_font = pt_text_font
                pt_str_w, pt_str_h = pt_text_dc.GetTextExtent(pt_str)
            else:
                pt_str = str(n)
                pt_color = pt_num_color
                pt_font = pt_num_font
                pt_str_w, pt_str_h = pt_num_dc.GetTextExtent(pt_str)
            pt = points[i]
            pt_coord = wx.Point(int(pt.x-pt_str_w/2), int(pt.y-pt_str_h/2))

            pt_strs.append(pt_str)
            pt_coords.append(pt_coord)
            pt_fonts.append(pt_font)
            pt_colors.append(wx.Colour(pt_color))
            dc.SetFont(pt_font)
            dc.SetTextForeground(wx.Colour(pt_color))
            dc.DrawText(text=pt_str, pt=pt_coord)

        title_texts = ["Line connecting random points",
                       "which are subsequently marked"]
        ti = 0
        for tline in title_texts:
            title_font = wx.Font(wx.FontInfo(14))   # tkinter uses 20
            dc = wx.PaintDC(self)
            dc.SetFont(title_font)
            title_w, title_h = dc.GetTextExtent(tline)
            title_pt = wx.Point(int(x_mid - title_w / 2), int(y_min+(ti-2)*title_h))
            dc.SetTextForeground(wx.Colour("violet"))
            dc.DrawText(text=tline, pt=title_pt)
            ti += 1



app = wx.App()
cvf = CanvasFrame(None)  # Alternative - master frame instead of master window
cvf.SetInitialSize(wx.Size(cv_width, cv_height))
cvf.Show()

app.MainLoop()

