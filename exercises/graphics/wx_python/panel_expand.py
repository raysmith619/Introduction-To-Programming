# panel_expand.py 
import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour("red")
        '''
        panel1 = wx.Panel(self)


        sizer_h = wx.BoxSizer(wx.HORIZONTAL)
        sizer_v = wx.BoxSizer(wx.VERTICAL)

        sizer_h.Add(panel1, 1, wx.EXPAND)
        sizer_v.Add(sizer_h, proportion=1, flag=wx.EXPAND)
        # only set the main sizer if you have more than one
        self.SetSizer(sizer_v)
        '''
        self.Show()

class MyFrame(wx.Frame):
    def __init__(self, title=None, size=None):
        """Constructor"""
        wx.Frame.__init__(self, None, title=title,
                          size=size)
        
        #panel1 = MyPanel(self)
        panel1 = wx.Panel(self)
        self.SetBackgroundColour("green")

        sizer_h = wx.BoxSizer(wx.HORIZONTAL)
        sizer_v = wx.BoxSizer(wx.VERTICAL)

        sizer_h.Add(panel1, 1, wx.EXPAND)
        sizer_v.Add(sizer_h, proportion=1, flag=wx.EXPAND)
        # only set the main sizer if you have more than one
        self.SetSizer(sizer_v)
        
        self.Show()
    
app = wx.App()
mytitle = "wx.Frame & wx.Panels"
width = 400
height = 500
frame = MyFrame(title=mytitle, size=wx.Size(width,height))
frame.Show()
panel = MyPanel(frame)
#panel.Show()
app.MainLoop()