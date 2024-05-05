#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this example we create review
layout with wx.FlexGridSizer.

author: Jan Bodnar
website: www.zetcode.com
last modified: April 2018
"""

import wx

class LabelEntry(wx.Frame):

    def __init__(self, parent=None, title="", prompt="", default="", on_input=None):
        """ Setup entry with label
        :parent: parent window
        :title: window title
        :prompt: optional prompt (label)
        :default: default value default: ''
        :on_input: function to call with input default: print value
        """
        super(LabelEntry, self).__init__(parent, title=title)
        self.prompt = prompt
        self.default = default
        self.on_input = on_input
        self.InitUI()
        self.Centre()
        self.Show()

    def OnEnter(self, e):
        """ Process ENTER
        """
        value = self.entry.GetValue()
        if self.on_input:
            self.on_input(value)
            return
        
        print(f"Entered: '{value}'")


    def InitUI(self):

        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(1, 2, 2, 2)

        label = wx.StaticText(panel, label=self.prompt)
        self.entry = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        entry_id = self.entry.GetId()
        self.entry.Bind(wx.EVT_TEXT_ENTER, self.OnEnter,self.entry)
        fgs.AddMany([(label), (self.entry, 1, wx.EXPAND)])
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)


def main():
    import sys
    
    def on_input(value):
        print(f"Input:{value}")
        if value.lower() == "quit":
            sys.exit()

    app = wx.App()
    le = LabelEntry(None, title='Label Entry', prompt="Enter:", on_input=on_input)
    app.MainLoop()


if __name__ == '__main__':

    main()
