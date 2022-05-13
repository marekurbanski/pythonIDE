import wx
import wx.html2


class MyBrowser(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("Zoom Christchurch NZ")

        filemenu = wx.Menu()
        filemenu.Append(1, "Some option")
        filemenu.Append(2, "Another option")
        filemenu.Append(3, "&Quit")
        menubar = wx.MenuBar()
        menubar.Append(filemenu, "&File")
        self.SetMenuBar(menubar)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.browser = wx.html2.WebView.New(self)
        Url = wx.FileSystem.FileNameToURL('maparea.html')
        self.browser.LoadURL(Url)
        self.sheesh = wx.Button(self, wx.ID_ANY, 'sheesh')

        sizer.Add(self.sheesh, 0, wx.ALIGN_TOP)
        sizer.Add(self.browser, 1, wx.EXPAND, 10)

        wx.EvtHandler.Bind(self, wx.html2.EVT_WEBVIEW_ERROR, self.BrowserError)
        filemenu.Bind(wx.EVT_MENU, self.OnQuit, id=3)  # Window closed using the Menu Quit option
        self.sheesh.Bind(wx.EVT_BUTTON, self.OnButton)
        self.Bind(wx.EVT_CLOSE, self.OnQuit)  # Window closed using the Title bar X

        self.SetSizer(sizer)
        self.SetSize((640, 360))

    def BrowserError(self, event):
        print("Error loading map")

    def OnButton(self, event):
        print("Button Pressed")

    def OnQuit(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = MyBrowser(None)
    frame.Show()
    app.MainLoop()