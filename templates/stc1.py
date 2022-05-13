import wx
import wx.stc as stc

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.tc = stc.StyledTextCtrl(self, style=wx.TE_MULTILINE | wx.TE_WORDWRAP)
        self.bt_find = wx.Button(self, -1, "find")

        self.Bind(wx.EVT_BUTTON, self.on_button, self.bt_find)
        self.Bind(wx.EVT_FIND, self.on_find)

        self.pos = 0
        self.size = 0
        #
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tc, 1, wx.EXPAND, 0)
        sizer.Add(self.bt_find, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()

    def on_button(self, event):
        self.txt = self.tc.GetValue()
        self.data = wx.FindReplaceData()   # initializes and holds search parameters
        dlg = wx.FindReplaceDialog(self.tc, self.data, 'Find')
        dlg.Show()

    def on_find(self, event):
        self.tc.StartStyling(pos=0, mask=0xFF)
        self.tc.SetStyling(length=len(self.txt), style=0)
        fstring = event.GetFindString()
        self.size = len(fstring)
        while True:
            self.pos = self.txt.find(fstring, self.pos)
            if self.pos < 0:
                break
            self.tc.StyleSetSpec(1, "fore:#FF0000,back:#000000")
            self.tc.StartStyling(pos=self.pos, mask=0xFF)
            self.tc.SetStyling(length=self.size, style=1)
            self.pos += 1
        self.pos = 0

if __name__ == "__main__":

    app = wx.App()
    frame_1 = MyFrame(None, wx.ID_ANY, "")
    frame_1.Show()
    app.MainLoop()