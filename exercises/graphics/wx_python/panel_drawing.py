# panel_drawing.py  05Nov2023  crs
# From FogleBird on Stackoverflow
"""
Here is some documentation on the drawing context functions:
http://www.wxpython.org/docs/api/wx.DC-class.html    
"""
import wx

class View(wx.Panel):
    def __init__(self, parent):
        super(View, self).__init__(parent)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_PAINT, self.on_paint)
    def on_size(self, event):
        event.Skip()
        self.Refresh()
    def on_paint(self, event):
        w, h = self.GetClientSize()
        dc = wx.AutoBufferedPaintDC(self)
        dc.Clear()
        dc.DrawLine(0, 0, w, h)
        dc.SetPen(wx.Pen(wx.BLACK, 5))
        cir_size = int(min(w,h)/4)
        dc.DrawCircle(w // 2, h // 2, cir_size)

class Frame(wx.Frame):
    def __init__(self):
        super(Frame, self).__init__(None)
        self.SetTitle('My Title')
        self.SetClientSize((500, 500))
        self.Center()
        self.view = View(self)

def main():
    app = wx.App(False)
    frame = Frame()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()