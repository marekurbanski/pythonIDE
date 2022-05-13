import wx
import wx.richtext
from io import BytesIO



class TabPanel(wx.Panel):
    def __init__(self, parent, name):
        """"""
        super().__init__(parent=parent)
        self.name = name
        #colors = ["red", "blue", "gray", "yellow", "green"]
        #self.SetBackgroundColour(random.choice(colors))
        #btn = wx.Button(self, label="Press Me")
        #sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(btn, 0, wx.ALL, 10)
        #self.SetSizer(sizer)



class EditFrame(wx.Frame):
    def __init__(self, parent):
        #wx.Frame.__init__(self, None, title='Richtext Test')
        #super(EditFrame, self).__init__(parent)

        panelLogs = wx.Panel(parent)
        size = panelLogs.FromDIP((200, 400))
        panelLogs.SetSize(size)

        self.notebookBottom = wx.Notebook(panelLogs)
        # self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_tab_change)
        tabLog = TabPanel(self.notebookBottom, name='Tab 1')
        self.notebookBottom.AddPage(tabLog, "Logs")

        sizerBottom = wx.BoxSizer(wx.VERTICAL)
        sizerBottom.Add(self.notebookBottom, 1, wx.ALL | wx.EXPAND, 5)
        panelLogs.SetSizer(sizerBottom)

        self.textLog = wx.TextCtrl(tabLog, -1, "Starting...\n", style=wx.NO_BORDER | wx.TE_MULTILINE)
        pbox = wx.BoxSizer(wx.HORIZONTAL)
        pbox.Add(self.textLog, 1, flag=wx.EXPAND)
        tabLog.SetSizer(pbox)


        #self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_tab_change)


        #self.rt.SetMinSize((300,200))
        #self.rt.Bind(wx.richtext.EVT_RICHTEXT_CHARACTER,self.textEdit)

        #self.Show()


    def textEdit(self, event):
        char = event.GetCharacter()
        pos = event.GetPosition()

        print("Clicked="+char+", pos_x="+str(pos))
        cp = self.rt.GetCaret().GetPosition()
        print("Cursor pos="+str(cp))
        cs = self.rt.GetCaret()
        print("Cursor pos="+str(cs))


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="pyTable", size=(335, 252))
        f = EditFrame(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()

