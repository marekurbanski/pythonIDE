import wx
import wx.aui

windowWidth = 10
windowHeight = 0

def change_size(frame):
    frame.SetSize(wx.Size(100, 100))

def size_change(event):
    width, height = event.GetSize()
    mainIDE.windowWidth = width
    windowHeight = height
    print("Width =", windowWidth, "Height =", windowHeight)


class mainIDE(wx.Frame):

    windowWidth = 44

    def OnQuit(self, e):
        self.Close()

    def addLog(self, message):
        self.textLog.WriteText(message+"\n")


    def __init__(self, parent, windowWidth, windowHeight):
        super(mainIDE, self).__init__(parent)
        wx.Panel.__init__(self, parent)
        #print(parent.GetSize())
        self.SetSize((200,200))
        self.SetTitle('PythonIDE')
        self.Centre()
        #wx.Window.Bind(wx.EVT_SIZE, self.size_change2())


        self.button = wx.Button(self, label="Open Message Box", pos=(100, 100))
        self.Bind(wx.EVT_BUTTON, self.messageBox)

#        print(wx.Panel.GetSize())
        self.Centre()
        self.Show(True)
        self.mgr = wx.aui.AuiManager(self)

    def messageBox(self, event):
        # wx.MessageBox('Message Box Dialog Info Icon', 'Dialog', wx.OK | wx.ICON_INFORMATION)
        # wx.MessageBox('Message Box Dialog Warning Icon', 'Dialog', wx.OK | wx.ICON_WARNING)
        # wx.MessageBox(str(self.windowWidth), 'Dialog', wx.OK | wx.ICON_ERROR)
        change_size(self)



app = wx.App(False)
mainide = mainIDE(None, windowWidth, windowHeight)
mainide.Bind(wx.EVT_SIZE, size_change)
app.MainLoop()

