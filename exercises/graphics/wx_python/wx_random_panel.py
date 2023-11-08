#wx_random_panel.py  05Nov2023
# Mike Driscoll on Stack Overflow

import random
import wx

########################################################################
class RandomPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        color = random.choice(["green", "blue", "yellow", "red"])
        self.SetBackgroundColour(color)

########################################################################
class MainPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        firstSubPanel = RandomPanel(self)
        secondSubPanel = RandomPanel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(firstSubPanel, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(secondSubPanel, 1, wx.EXPAND|wx.ALL, 5)
        self.SetSizer(sizer)

########################################################################
class MainFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Panels")

        panel = MainPanel(self)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()