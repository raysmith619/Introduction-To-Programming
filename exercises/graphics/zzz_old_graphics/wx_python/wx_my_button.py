# wx_my_button.py       13Jun2023  crs, From my_button.py
import wx


def ok_cmd(e):
    print("ok_cmd")


def not_ok_cmd(e):
    print("not_ok_cmd")


def quit_cmd(e):
    print("quit_cmd")
    wx.Exit()


app = wx.App()
frame = wx.Frame(None)
frame.Show()
panel = wx.Panel(frame)
btn_height = 50
btn_width = int(1.5 * btn_height)

ok_height = btn_height
ok_width = btn_width

not_ok_height = int(1.5 * btn_height)
not_ok_width = btn_width

quit_height = int(2 * btn_height)
quit_width = btn_width
pos_1 = wx.Point(int(btn_width/2),btn_height)
btn_inc = wx.Size(btn_width,0)
ok_button = wx.Button(panel, label="OK", pos=pos_1,
                      size=(ok_width, ok_height))
ok_button.Bind(wx.EVT_BUTTON, ok_cmd)
ok_button.SetForegroundColour(wx.GREEN)
ok_button.SetBackgroundColour(wx.LIGHT_GREY)

not_ok_pos = pos_1 + btn_inc
not_ok_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, 0,90)
not_ok_button = wx.Button(panel, label="Not OK", pos=not_ok_pos,
                          size=(not_ok_width, not_ok_height))
not_ok_button.SetFont(not_ok_font)
not_ok_button.Bind(wx.EVT_BUTTON, not_ok_cmd)
not_ok_button.SetForegroundColour(wx.BLUE)
not_ok_button.SetBackgroundColour(wx.LIGHT_GREY)

quit_pos = not_ok_pos + btn_inc
quit_font = wx.Font(18, wx.FONTFAMILY_DEFAULT, 0,90)
quit_button = wx.Button(panel, label="QUIT", pos=quit_pos,
                        style=wx.BORDER_RAISED,
                        size=(quit_width, quit_height))
quit_button.SetFont(quit_font)
quit_button.Bind(wx.EVT_BUTTON, quit_cmd)
quit_button.SetForegroundColour(wx.RED)
quit_button.SetBackgroundColour(wx.LIGHT_GREY)

frame.SetSize((350, 250))
frame.SetTitle('wx_my_button')
frame.Centre()

app.MainLoop()
print("After mainloop")
