#wx_my_frame.py    13Jun2023  crs, from my_frame.py
"""
Simple layout using wxPython
Three lines with increasing number of labels
"""
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        our_ptsize = 10
        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(our_ptsize)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        label_1_1 = wx.StaticText(panel, label='Label_1_1')
        label_1_1.SetFont(font)
        hbox1.Add(label_1_1, flag=wx.RIGHT, border=8)
        vbox.Add(hbox1, proportion=0, flag=wx.ALIGN_CENTER_HORIZONTAL,
                 border=10)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        label_2_1 = wx.StaticText(panel, label='Label_2_1')
        label_2_1.SetFont(font)

        hbox2.Add(label_2_1, flag=wx.RIGHT, border=8)

        label_2_2 = wx.StaticText(panel, label='Label_2_2')
        label_2_2.SetFont(font)
        hbox2.Add(label_2_2, flag=wx.RIGHT, border=8)
        vbox.Add(hbox2, proportion=2, flag=wx.ALIGN_CENTER_HORIZONTAL, border=10)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        label_3_1 = wx.StaticText(panel, label='Label_2_1')
        label_3_1.SetFont(font)
        hbox3.Add(label_3_1, flag=wx.RIGHT, border=8)

        label_3_2 = wx.StaticText(panel, label='Label_3_2')
        label_3_2.SetFont(font)
        hbox3.Add(label_3_2, flag=wx.RIGHT, border=8)

        label_3_3 = wx.StaticText(panel, label='Label_3_3')
        label_3_3.SetFont(font)
        hbox3.Add(label_3_3, flag=wx.RIGHT, border=8)
        vbox.Add(hbox3, proportion=3,flag=wx.ALIGN_CENTRE_HORIZONTAL,
                 border=10)

        panel.SetSizer(vbox)

def main():
    app = wx.App()
    ex = Example(None, title="wxPython version of my_frame.py")
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    # keep the window displaying
    main()
