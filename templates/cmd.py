import wx
import wx.py

app = wx.App(False)
frm = wx.Frame(None, -1, "wxPyShell")
wx.py.shell.Shell(frm)
frm.Show()
app.MainLoop()