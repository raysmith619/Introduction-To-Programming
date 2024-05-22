#wx_gr_input.py    09Jun2023  crs, from https://pythonspot.com/wxpython-input-dialog/

import wx

def gr_input(prompt=None, default="", frame=None):
    local_frame = False     # Set True if make our own
    if frame is None:
        local_frame = True
        frame = wx.Frame(None, -1, 'win.py', size=wx.Size(200,50))
        frame.Show()

    # Create text input
    dlg = wx.TextEntryDialog(frame, prompt,'Text Entry')
    dlg.SetValue(default)
    value = default
    if dlg.ShowModal() == wx.ID_OK:
        value = dlg.GetValue()
        dlg.Destroy()
        if local_frame:
            frame.Destroy()
        return value

    dlg.Destroy()
    if local_frame:
        frame.Destroy()

    return value



if __name__ == "__main__":
    app = wx.App()
    inp = gr_input(prompt="Enter Guess")
    print(f"Entered: '{inp}'")

    inp = gr_input(prompt="Next Guess")
    print(f"Entered: '{inp}'")

    app.MainLoop()



