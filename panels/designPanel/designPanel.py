import wx
from pubsub import pub
import wx.richtext
import re
import wx.stc as stc

##
## Fix for autofill textBox - strech
def change_size(frame):
    size = frame.GetSize()
    w = size[0]
    h = size[1]
    frame.SetSize(wx.Size(w-1, h))
    frame.SetSize(wx.Size(w, h))


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


class designPanel(wx.Panel):

    appWidth = 10
    appHeight = 10

    def setData(self, notebookEdit, panelDesign, panelDesignEdit, panelComponents, pboxNotebookEdit):

        self.notebookEdit = notebookEdit
        self.panelDesign = panelDesign
        self.panelDesignEdit = panelDesignEdit
        self.panelComponents = panelComponents
        self.pboxNotebookEdit = pboxNotebookEdit


    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        #self.app = wx.App(False)
        self.d = {}

        print("Handler prepare")
        pub.subscribe(self.openTabFile, 'openTabFile')
        print("Handler set")
        #parent.Layout()
        #parent.Show()


    def openTabFile(self, message):
        print("Opening "+message)

        full_path = message
        message = message[::-1].split("/")[0][::-1]
        tabLog2 = TabPanel(self.notebookEdit, name=message)
        self.notebookEdit.AddPage(tabLog2, "File:"+message)

        #sizerBottom2 = wx.BoxSizer(wx.VERTICAL)
        #sizerBottom2.Add(self.notebookEdit, 1, wx.ALL | wx.EXPAND, 1)
        #self.panelDesignEdit.SetSizer(sizerBottom2)
        #self.panelDesignEdit.Refresh()

        self.textBox = wx.richtext.RichTextCtrl(tabLog2, -1, "Starting...\n", style=wx.NO_BORDER | wx.TE_MULTILINE | wx.TE_DONTWRAP | wx.HSCROLL)
        self.textBox.Bind(wx.EVT_CHAR_HOOK, self.OnKeyWhich, self.textBox)
        #btn.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)
        pbox2 = wx.BoxSizer(wx.VERTICAL)
        pbox2.Add(self.textBox, 1, wx.ALL | wx.EXPAND, 1)

        tabLog2.SetSizer(pbox2)
        tabLog2.Show()
        tabLog2.Refresh()
        self.textBox.Clear();
        f = open(full_path, 'r')
        content = f.read()
        f.close();

        self.textBox.WriteText(content)
        self.colorize()

        change_size(self.parent.GetParent().GetParent())
        #size = self.panelDesign.FromDIP((w,h))
        #self.panelDesign.SetSize(size)

        #self.panelDesignEdit.Refresh()

    def OnKeyWhich(self, event):
        key = event.GetKeyCode()
        print("Clicked: "+str(key))
        #if key == wx.WXK_RETURN:
        #    self.update_result()
        #else:
        #    event.Skip()
        event.Skip()
        self.colorize()

    def colorize(self,):
        colour_black = wx.TextAttr(wx.BLACK)
        self.textBox.SetStyle(0, 100000000, colour_black)

        words = ['import','from','def','return','class','try','except','pass']
        word_colour = wx.TextAttr(wx.BLUE)
        content = self.textBox.GetValue()
        for word in words:
            word_occurs = self.find_str(word, content)
            for i in word_occurs:
                # SetStyle(start pos, end pos, style)
                self.textBox.SetStyle(i, i + len(word), word_colour)

        word = '(\d+)'
        word_colour = wx.TextAttr(wx.RED)
        content = self.textBox.GetValue()
        word_occurs = self.find_str(word, content)
        for i in word_occurs:
            # SetStyle(start pos, end pos, style)
            self.textBox.SetStyle(i, i + len(word), word_colour)

        word = 'wx\.\w+'
        word_colour = wx.TextAttr(wx.Colour(100, 100, 100))
        content = self.textBox.GetValue()
        word_occurs = self.find_str(word, content)
        for i in word_occurs:
            # SetStyle(start pos, end pos, style)
            self.textBox.SetStyle(i, i + len(word), word_colour)
            #self.textBox.SetFont(wx.Font(12, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD, faceName='Consolas'))


    def find_str(self, sub, sent):  # return positions of the word
        return [x.start() for x in re.finditer(sub, sent)]


    def addTestItem(self):
        box = wx.BoxSizer(wx.VERTICAL)
        self.button1 = wx.Button(self.parent, -1, "foo")
        box.Add(self.button1, 0, wx.ALL, 10)
        self.button2 = wx.Button(self.parent, -1, "bar")
        box.Add(self.button2, 0, wx.ALL, 10)

        self.button1.Bind(wx.EVT_LEFT_DOWN, self.MouseDown)
        self.button2.Bind(wx.EVT_LEFT_DOWN, self.MouseDown)

        self.button1.Bind(wx.EVT_MOTION, self.MouseMove)
        self.button2.Bind(wx.EVT_MOTION, self.MouseMove)

        self.button1.Bind(wx.EVT_LEFT_UP, self.MouseUp)
        self.button2.Bind(wx.EVT_LEFT_UP, self.MouseUp)
        #self.parent.Bind(wx.EVT_MOTION, self.MouseMove)
        #self.parent.Bind(wx.EVT_LEFT_UP, self.MouseUp)


        self.parent.SetSizer(box)

    def wMouseDown(self, e):
        print ("!!!", e.GetEventObject())

    def MouseDown(self, e):
        o           = e.GetEventObject()
        sx,sy       = self.parent.ScreenToClient(o.GetPosition())
        dx,dy       = self.parent.ScreenToClient(wx.GetMousePosition())
        o._x,o._y   = (sx-dx, sy-dy)
        self.d['d'] = o

    def MouseMove(self, e):
        try:
            if 'd' in self.d:
                o = self.d['d']
                x, y = wx.GetMousePosition()
                o.SetPosition(wx.Point(x+o._x,y+o._y))
        except:
            print("ErrorA")
            pass

    def MouseUp(self, e):
        try:
            if 'd' in self.d:
                o = e.GetEventObject()
                print(str(e))
                sx, sy = o.ScreenToClient(o.GetPosition())
                dx, dy = o.ScreenToClient(wx.GetMousePosition())
                print("x=" + str(sx) + "; y=" + str(sy))
                del self.d['d']
        except:
            print("ErrorB")
            o = e.GetEventObject()
            sx, sy = self.panel.ScreenToClient(o.GetPosition())
            dx, dy = self.panel.ScreenToClient(wx.GetMousePosition())
            print("x=" + str(sx) + "; y=" + str(sy))
            pass



