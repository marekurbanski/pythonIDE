import wx
import wx.aui

def CreateMenu(self):

    menubar = wx.MenuBar()

    # Menu column start
    fileMenu = wx.Menu()

    newitem = wx.MenuItem(fileMenu, wx.ID_NEW, text="File", kind=wx.ITEM_NORMAL)
    # newitem.SetBitmap(wx.Bitmap("new.bmp"))
    fileMenu.AppendItem(newitem)
    fileMenu.AppendSeparator()

    newitem2 = wx.MenuItem(fileMenu, wx.ID_NEW, text="File2", kind=wx.ITEM_NORMAL)
    # newitem.SetBitmap(wx.Bitmap("new.bmp"))
    fileMenu.AppendItem(newitem2)
    fileMenu.AppendSeparator()

    menubar.Append(fileMenu, '&File')
    # Menu column stop



    # Menu column start
    optionsMenu = wx.Menu()

    newitem3 = wx.MenuItem(optionsMenu, wx.ID_NEW, text="File3", kind=wx.ITEM_NORMAL)
    # newitem.SetBitmap(wx.Bitmap("new.bmp"))
    optionsMenu.Append(newitem3)
    optionsMenu.AppendSeparator()

    menubar.Append(optionsMenu, '&Option')
    # Menu column stop


    self.SetMenuBar(menubar)
