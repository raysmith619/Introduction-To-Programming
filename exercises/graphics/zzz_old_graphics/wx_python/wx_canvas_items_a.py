#wx_canvas_items.py 08Jun2023  crs, from canvas_items.py
#canvas_items.py    23Oct2022  crs, From resource_lib_proj/
"""
wxPython version of tkinter Canvas items examples
Note wxPython does not have a Canvas widget which exists in tkinter
Thanks to Jan Bodnar (zetcode.com) for his wxPython examples on which I've drawn

"""
import wx
cv_width = 300
cv_height = cv_width*2
x_min = cv_width*.1
x_max = cv_width*.9
x_mid = (x_min+x_max)/2
y_min = cv_height*.1
y_max = cv_height*.9
y_mid = (y_min+y_max)/2

def OnPaint(e):
    """ Non-object paint call
        Paints our picture
        :e: event
        """
    dc = wx.PaintDC(mf)
    dc.SetPen(wx.Pen("green", style=wx.TRANSPARENT))
    dc.SetBrush(wx.Brush("green", wx.SOLID))
    dc.DrawRectangle(x_min, y_min, x_max, y_max)
    ###mf.Show()
    '''
    line = canvas.create_line(x_min,y_min,
                              x_max,y_max, fill="red",
                              width=10)
    line2 = canvas.create_line(x_min,y_max,
                               x_max, y_min, fill="blue")
    oval = canvas.create_oval(x_mid,y_min, x_max, y_max,
                              fill="orange")
    x_q = (x_min+x_mid)/2
    y_q = (y_min+y_mid)/2
    sq = canvas.create_rectangle(x_q, y_q,
                                 x_mid, y_mid,
                                 fill="yellow")
    canvas.create_text(x_mid,y_mid, text="Hello World",
                       font="Tahoma 30")
    '''


app = wx.App()

mf = wx.Frame(None)         # Alternative - master frame instead of master window
mf.Bind(wx.EVT_PAINT, OnPaint)

mf.SetTitle('wxPython "canvas" items_a')
mf.Centre()
mf.Show()

app.MainLoop()


