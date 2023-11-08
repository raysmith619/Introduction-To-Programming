#wx_canvas_items_flex.py    02Jul2023  crs, from wx_canvas_items.py
#                           08Jun2023  crs, from canvas_items.py
#canvas_items.py    23Oct2022  crs, From resource_lib_proj/
"""
Proportionaly change enclosed figures when window is resized
wxPython version of tkinter Canvas items examples
Note wxPython does not have a Canvas widget which exists in tkinter
Thanks to Jan Bodnar (zetcode.com) for his wxPython examples on which I've drawn

"""
import wx

cv_width = 300
cv_height = cv_width*2


class CanvasFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(CanvasFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle("wxPython Canvas shapes")
        self.Centre()

    def OnPaint(self, e):
        global color_idx
        
        size=self.GetClientSize()
        cv_w = size.width
        cv_h = size.height
        print(f"OnPaint cv_w:{cv_w} cv_h:{cv_h}")
        x_min = int(cv_w*.1)
        x_max = int(cv_w*.9)
        pat_width = x_max-x_min
        x_mid = int((x_min+x_max)/2)

        y_min = int(cv_h*.1)
        y_max = int(cv_h*.9)
        y_mid = int((y_min+y_max)/2)
        pat_height = y_max-y_min
        dc = wx.PaintDC(self)
        dc.Clear()

        
        dc.SetPen(wx.Pen("green", style=wx.TRANSPARENT))
        dc.SetBrush(wx.Brush("green", wx.SOLID))
        dc.DrawRectangle(x_min, y_min, pat_width, pat_height)

        thickness = 10
        pen = wx.Pen(wx.Colour("red"), thickness, wx.SOLID)
        dc.SetPen(pen)
        dc.DrawLine(x_min,y_min, x_max,y_max)

        dc.SetPen(wx.Pen("blue", style=wx.SOLID))
        dc.SetBrush(wx.Brush("blue", wx.SOLID))
        dc.DrawLine(x_min,y_max, x_max,y_min)

        dc.SetPen(wx.Pen("orange", style=wx.SOLID))
        dc.SetBrush(wx.Brush("orange", wx.SOLID))
        dc.DrawEllipse(x_mid, y_min, x_max-x_mid, y_max-y_min)
        print(f"DrawEllipse({x_mid},{y_mid},{x_max-x_mid}, {y_max-y_min})")
    
        x_q = int((x_min+x_mid)/2)
        y_q = int((y_min+y_mid)/2)
        dc.SetPen(wx.Pen("black", style=wx.SOLID))
        dc.SetBrush(wx.Brush("yellow", wx.SOLID))
        dc.DrawRectangle(x_q, y_q, int(pat_width/4), int(pat_height/4))

        dc.SetPen(wx.Pen("black", style=wx.SOLID))
        dc.SetBrush(wx.Brush("yellow", wx.TRANSPARENT))
        title_text = "Hello World"
        title_font = wx.Font(wx.FontInfo(30))
        dc.SetFont(title_font)
        title_w,title_h = dc.GetTextExtent(title_text)
        title_pt = wx.Point(int(x_mid-title_w/2), int(y_mid-title_h/2))
        dc.DrawText(text=title_text, pt=title_pt)
        #dc.Refresh()



app = wx.App()

cvf = CanvasFrame(None)         # Alternative - master frame instead of master window
cvf.SetInitialSize(wx.Size(cv_width, cv_height))
cvf.Show()

app.MainLoop()


