
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

y_min = int(cv_height*.1)
y_max = int(cv_height*.9)
y_mid = int((y_min+y_max)/2)
pat_height = y_max-y_min

x_range = (x_max-x_min)
y_range = abs(y_max-y_min)



# parabola: f(x) = x**2
# Scale to fit (x,y: min to max)
# x increases to right
# y increases down
npts = 100
points = []    # List of wx.Point
fn_x_max = npts-1
fn_y_max = fn_x_max**2
for i in range(npts):
    fn_x = i
    fn_y = fn_x**2
    x = int(x_min + x_range*fn_x/fn_x_max)
    y = int(y_min + y_range*fn_y/fn_y_max)
    point = wx.Point(x,y)
    points.append(point)


class CanvasFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(CanvasFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle("wxPython Canvas lines")
        self.Centre()

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        thickness = 5
        pen = wx.Pen(wx.Colour("red"), thickness, wx.SOLID)
        dc.SetPen(pen)
        dc.DrawLines(points)


        title_text = "Parabola"
        title_font = wx.Font(wx.FontInfo(20))
        dc = wx.PaintDC(self)
        pen = wx.Pen(wx.Colour("blue"), thickness, wx.SOLID)
        dc.SetPen(pen)
        dc.SetFont(title_font)
        title_w, title_h = dc.GetTextExtent(title_text)
        title_pt = wx.Point(int(x_mid - title_w / 2), int(y_min-title_h))
        ###dc.DrawText(text=title_text, pt=title_pt)
        dc.DrawTextList(textList=[title_text], coords=[title_pt], foregrounds=[wx.Colour("blue")])


app = wx.App()
cvf = CanvasFrame(None)  # Alternative - master frame instead of master window
cvf.SetInitialSize(wx.Size(cv_width, cv_height))
cvf.Show()

app.MainLoop()

