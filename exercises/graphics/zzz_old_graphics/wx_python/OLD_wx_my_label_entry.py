#wx_my_label_entry.py    10Jun2023  crs, from my_entry.py
import wx

class GrLabelEntry(parent, prompt="Enter:", title=None, text=None, id=-1):
    def __init__(self, parent=parent, id=id, title=title):

        wx.Dialog(parent, wx.DefaultPosition, wx.DefaultSize,
                  wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER, id=id, title=title)

        label_sizer = wx.BoxSizer(wx.VERTICAL)

        # create text ctrl with minimal size 100x60
        label_sizer.Add(
                wx.TextCtrl(self, -1, prompt, wx.DefaultPosition, wx.Size(100,60), wx.TE_MULTILINE),
                1,           # make vertically stretchable
                wx.EXPAND |  # make horizontally stretchable
                wx.ALL,      # and make border all around
                10)          # set border width to 10

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(
                wx.Button(self, wx.ID_OK, "OK"),
                0,           # make horizontally unstretchable
                wx.ALL,      # make border all around (implicit top alignment)
                10)          # set border width to 10
        button_sizer.Add(
                wx.Button(self, wx.ID_CANCEL, "Cancel"),
                0,           # make horizontally unstretchable
                wx.ALL,      # make border all around (implicit top alignment)
                10)          # set border width to 10

        topsizer.Add(
                button_sizer,
                0,                # make vertically unstretchable
                wx.ALIGN_CENTER)  # no border and centre horizontally

        self.SetSizerAndFit(topsizer) # use the sizer for layout and size window
                                      # accordingly and prevent it from being resized

def gr_input(prompt="Enter:"):
    """ Prompt and recieve input from user
    :prompt: Prompt for input default: "Enter:"
    :returns: User input string, not including ENTER
        default: ""
    """
    

if __name__ == "__main__":
    app = wx.App()
    mf = wx.Frame(None)
    mf.Show()
    panel = wx.Panel(mf)
    gr_label_entry(panel, label="Our Label")
    # keep the window displaying
    app.MainLoop()
