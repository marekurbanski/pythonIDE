import wx
import wx.aui
import wx.py
import os
import sys
from pubsub import pub
from panels.menu import menu
import wx.lib.scrolledpanel
from classes import settingsClass as config
from classes import logClass
#from xml.dom import minidom
import random
# pip3 install PyPubSub
from panels.objectInspector import objectInspectorParams
from panels.projectFiles import projectFiles
from panels.designPanel import designPanel
import wx.richtext as richtext

applicationWidth = 1
applicationHeight = 1


def change_size(frame):
    frame.SetSize(wx.Size(100, 100))

def size_change(event):
    width, height = event.GetSize()
    applicationWidth = width
    applicationHeight = height
    print("Width =", width, "Height =", height)



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


class mainIDE(wx.Frame):

    applicationWidth = 0
    applicationHeight = 0

    def OnQuit(self, e):
        self.Close()

    def addLog(self, message):
        self.textLog.WriteText(message+"\n")


    def __init__(self, parent, title):
        super(mainIDE, self).__init__(parent)
        #logClass.log.Debug(self, "Starting IDE")
        #settingsClass.settings.LoadSettingsFile(self)
        self.applicationWidth = int(config.settings.get(self, 'mainWindow/dimension','width') or 600)
        self.applicationHeight = int(config.settings.get(self, 'mainWindow/dimension', 'height') or 400)

        self.SetSize((self.applicationWidth, self.applicationHeight))
        self.SetTitle('PythonIDE')
        self.Centre()

        # Main menu
        menu.CreateMenu(self)


        self.mgr = wx.aui.AuiManager(self)

        ############################################## Bottom LOG panel #################################################
        panelLogs = wx.Panel(self)
        h = int(config.settings.get(self, 'mainWindow/panels/logs', 'height') or 400)
        size = panelLogs.FromDIP((200, h))
        panelLogs.SetSize(size)

        self.notebookBottom = wx.Notebook(panelLogs)
        #self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_tab_change)
        tabLog = TabPanel(self.notebookBottom, name='Tab 1')
        self.notebookBottom.AddPage(tabLog, "Logs")
        tabTwo = TabPanel(self.notebookBottom, name='Tab 2')
        self.notebookBottom.AddPage(tabTwo, "Console")

        sizerBottom = wx.BoxSizer(wx.VERTICAL)
        sizerBottom.Add(self.notebookBottom, 1, wx.ALL | wx.EXPAND, 5)
        panelLogs.SetSizer(sizerBottom)

        self.textLog = wx.TextCtrl(tabLog, -1, "Starting...\n", style=wx.NO_BORDER | wx.TE_MULTILINE)
        pbox = wx.BoxSizer(wx.HORIZONTAL)
        pbox.Add(self.textLog, 1, flag=wx.EXPAND)
        tabLog.SetSizer(pbox)
        # eventHandler for adding logs
        pub.subscribe(self.addLog, 'add_log')


        #app = wx.App(False)
        #frm = wx.Frame(tabTwo, 1, "wxPyShell")
        #wx.py.shell.Shell(frm)
        #frm.Show()
        #app.MainLoop()
        #logClass.log.Debug(self, "IDE Started")

        ############################################## Left Files/Component panel #################################################

        panelComponents = wx.Panel(self,  style=wx.NO_BORDER)
        w = int(config.settings.get(self, 'mainWindow/panels/components', 'width') or 200)
        size = panelComponents.FromDIP((w, 200))
        panelComponents.SetSize(size)

        #### adding tabs
        self.notebookLeft = wx.Notebook(panelComponents)
        # self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_tab_change)
        tabFiles = TabPanel(self.notebookLeft, name='Tab 1')
        self.notebookLeft.AddPage(tabFiles, "Files")
        tabComponents = TabPanel(self.notebookLeft, name='Tab 2')
        self.notebookLeft.AddPage(tabComponents, "Components")

        pboxTabComponents = wx.BoxSizer(wx.VERTICAL)
        pboxTabComponents.Add(self.notebookLeft, 1, flag=wx.EXPAND)
        panelComponents.SetSizer(pboxTabComponents)

        ###### file tree ######
        filesTree = projectFiles.projectFiles(tabFiles)

        pboxFiles = wx.BoxSizer(wx.VERTICAL)
        pboxFiles.Add(filesTree.filesTree, 1, flag=wx.EXPAND)
        tabFiles.SetSizer(pboxFiles)



        #### scrollPanel for tabComponents
        panelComponentsScroll = wx.lib.scrolledpanel.ScrolledPanel(tabComponents, -1, size=(10, 10), pos=(0, 28), style=wx.NO_BORDER)
        panelComponentsScroll.SetupScrolling()
        panelComponentsScroll.SetSize(size)

        # label
        panelComponentLabel = wx.StaticText(panelComponentsScroll, id=1, label="Select component", pos=(0, 0), size=wx.DefaultSize, style=0, name="select_component")

        bSizer = wx.BoxSizer(wx.VERTICAL)
        bSizer.Add(panelComponentLabel, 0, wx.ALL, 0)
        # buttons
        for x in range(0, 30):
            bmp = wx.Bitmap('components/classic-button/icon.png')
            self.st = wx.Button(panelComponentsScroll, id=1, label=str(x) + "Classic Button", pos=(20, 20), size=(150, 30), name="button")
            self.st.SetBitmap(bmp)
            bSizer.Add(self.st, 0, wx.ALL, 0)
            #self.Centre()
        panelComponentsScroll.SetSizer(bSizer)

        pboxPanelComponents = wx.BoxSizer(wx.VERTICAL)
        pboxPanelComponents.Add(panelComponentsScroll, 1, flag=wx.EXPAND)
        tabComponents.SetSizer(pboxPanelComponents)

        #####

        panelFiles = wx.Panel(self,  style=wx.NO_BORDER)
        pbox6 = wx.BoxSizer(wx.VERTICAL)
        text3 = wx.TextCtrl(panelFiles, -1, "Place for structure tree with Designer Form", style=wx.NO_BORDER | wx.TE_MULTILINE)
        pbox6.Add(text3, 1, flag=wx.EXPAND)
        panelFiles.SetSizer(pbox6)

        ############################################## Right Object inspector / Structure  panel #################################################

        panelObjectInspectorStructure = wx.Panel(self,  style=wx.NO_BORDER)
        pbox3 = wx.BoxSizer(wx.VERTICAL)
        w = int(config.settings.get(self, 'mainWindow/panels/objectInspector', 'width') or 200)
        size = panelComponents.FromDIP((w, 200))
        panelObjectInspectorStructure.SetSize(size)

        #text3 = wx.TextCtrl(panelObjectInspectorStructure, -1, "Dockable3", style=wx.NO_BORDER | wx.TE_MULTILINE)
        #pbox3.Add(text3, 1, flag=wx.EXPAND)
        #panelObjectInspectorStructure.SetSizer(pbox3)

        #### adding tabs
        self.notebookRight = wx.Notebook(panelObjectInspectorStructure)
        # self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_tab_change)
        tabObjectInspector = TabPanel(self.notebookRight, name='Tab 1')
        self.notebookRight.AddPage(tabObjectInspector, "Object Inspector")
        tabObjectEvents = TabPanel(self.notebookRight, name='Tab 2')
        self.notebookRight.AddPage(tabObjectEvents, "Events")

        pboxTabObjectInspectorStructure = wx.BoxSizer(wx.VERTICAL)
        pboxTabObjectInspectorStructure.Add(self.notebookRight, 1, flag=wx.EXPAND)
        panelObjectInspectorStructure.SetSizer(pboxTabObjectInspectorStructure)

        x = objectInspectorParams.objectInspectorParams(tabObjectInspector)
        pbox = wx.BoxSizer(wx.VERTICAL)
        pbox.Add(x, 1, flag=wx.EXPAND)
        tabObjectInspector.SetSizer(pbox)



        pnl4 = wx.Panel(self,  style=wx.NO_BORDER)
        pbox4 = wx.BoxSizer(wx.VERTICAL)
        text4 = wx.TextCtrl(pnl4, -1, "Place for buttons like 'Run', 'Compile'...", style=wx.NO_BORDER | wx.TE_MULTILINE)
        pbox4.Add(text4, 1, flag=wx.EXPAND)
        pnl4.SetSizer(pbox4)

        ############################################## Panel for edit files / design objects #################################################
        panelDesignEdit = wx.Panel(self)
        pboxNotebookEdit = wx.BoxSizer(wx.VERTICAL)

        self.notebookEdit = wx.Notebook(panelDesignEdit)

        pboxNotebookEdit.Add(self.notebookEdit, 1, flag=wx.EXPAND)
        panelDesignEdit.SetSizer(pboxNotebookEdit)

        # self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_tab_change)


        # eventHandler for adding logs
        #pub.subscribe(self.addLog, 'add_log')

        designfiles = designPanel.designPanel(self.notebookEdit)
        """
        xOI,yOI = panelObjectInspectorStructure.GetSize()
        xPC, yPC = panelComponents.GetSize()
        xPL, yPL = panelLogs.GetSize()
        print(self.GetParent())
        parentWidth, parentHeight = panelLogs.GetSize()
        x = self.applicationWidth - xOI - xPC - 20
        y = self.applicationHeight - yPL - 120
        print(x,y)
        """
        #print("APP Size:",getAppSizeX())
        designfiles.setData(self.notebookEdit, panelDesignEdit, panelDesignEdit, panelComponents, pboxNotebookEdit)


        info1 = wx.aui.AuiPaneInfo().Bottom()
        info2 = wx.aui.AuiPaneInfo().Left()
        info3 = wx.aui.AuiPaneInfo().Right()
        info4 = wx.aui.AuiPaneInfo().Top()
        info5 = wx.aui.AuiPaneInfo().Center()
        info6 = wx.aui.AuiPaneInfo().Left()
        self.mgr.AddPane(panelLogs, info1)
        self.mgr.AddPane(panelComponents, info2)
        self.mgr.AddPane(panelObjectInspectorStructure, info3)
        self.mgr.AddPane(pnl4, info4)
        self.mgr.AddPane(panelDesignEdit, info5)
        self.mgr.AddPane(panelFiles, info6)



        #panel = wx.Panel(self)
        #text2 = wx.TextCtrl(panel, size=(300, 200), style=wx.NO_BORDER | wx.TE_MULTILINE)
        #box = wx.BoxSizer(wx.HORIZONTAL)
        #box.Add(text2, 1, flag=wx.EXPAND)

        #panel.SetSizerAndFit(box)
        self.mgr.Update()

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Centre()
        self.Show(True)

        logClass.log.Debug(self, "IDE Started")

    def OnClose(self, event):
        self.mgr.UnInit()
        self.Destroy()


app = wx.App(False)
mainide = mainIDE(None, "PythonIDE")
mainide.Bind(wx.EVT_SIZE, size_change)
app.MainLoop()