import wx
import wx.aui


class Mywin(wx.Frame):

    def OnQuit(self, e):
        self.Close()

    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent)
        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        self.Centre()

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        newitem = wx.MenuItem(fileMenu, wx.ID_NEW, text="New", kind=wx.ITEM_NORMAL)
        #newitem.SetBitmap(wx.Bitmap("new.bmp"))
        fileMenu.AppendItem(newitem)
        fileMenu.AppendSeparator()

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.mgr = wx.aui.AuiManager(self)

        pnl = wx.Panel(self)
        pbox = wx.BoxSizer(wx.HORIZONTAL)
        text1 = wx.TextCtrl(pnl, -1, "Dockable", style=wx.NO_BORDER | wx.TE_MULTILINE)
        pbox.Add(text1, 1, flag=wx.EXPAND)
        pnl.SetSizer(pbox)


        pnl2 = wx.Panel(self)
        pbox2 = wx.BoxSizer(wx.VERTICAL)
        text2 = wx.TextCtrl(pnl2, -1, "Dockable2", style=wx.NO_BORDER | wx.TE_MULTILINE)
        pbox2.Add(text2, 1, flag=wx.EXPAND)
        pnl2.SetSizer(pbox2)

        pnl3 = wx.Panel(self)
        pbox3 = wx.BoxSizer(wx.VERTICAL)
        text3 = wx.TextCtrl(pnl3, -1, "Dockable3", style=wx.NO_BORDER | wx.TE_MULTILINE)
        pbox3.Add(text3, 1, flag=wx.EXPAND)
        pnl3.SetSizer(pbox3)

        pnl4 = wx.Panel(self)
        pbox4 = wx.BoxSizer(wx.VERTICAL)
        text4 = wx.TextCtrl(pnl4, -1, "Dockable4", style=wx.NO_BORDER | wx.TE_MULTILINE)
        pbox4.Add(text4, 1, flag=wx.EXPAND)
        pnl4.SetSizer(pbox4)

        pnl5 = wx.Panel(self)
        pbox5 = wx.BoxSizer(wx.VERTICAL)
        text5 = wx.TextCtrl(pnl5, -1, "Dockable5", style=wx.NO_BORDER | wx.TE_MULTILINE)
        pbox5.Add(text5, 1, flag=wx.EXPAND)
        pnl5.SetSizer(pbox5)


        info1 = wx.aui.AuiPaneInfo().Bottom()
        info2 = wx.aui.AuiPaneInfo().Left()
        info3 = wx.aui.AuiPaneInfo().Right()
        info4 = wx.aui.AuiPaneInfo().Top()
        info5 = wx.aui.AuiPaneInfo().Center()
        self.mgr.AddPane(pnl, info1)
        self.mgr.AddPane(pnl2, info2)
        self.mgr.AddPane(pnl3, info3)
        self.mgr.AddPane(pnl4, info4)
        self.mgr.AddPane(pnl5, info5)

        #panel = wx.Panel(self)
        #text2 = wx.TextCtrl(panel, size=(300, 200), style=wx.NO_BORDER | wx.TE_MULTILINE)
        #box = wx.BoxSizer(wx.HORIZONTAL)
        #box.Add(text2, 1, flag=wx.EXPAND)

        #panel.SetSizerAndFit(box)
        self.mgr.Update()

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Centre()
        self.Show(True)

    def OnClose(self, event):
        self.mgr.UnInit()
        self.Destroy()


app = wx.App()
Mywin(None, "Dock Demo")
app.MainLoop()