import wx

class designPanel(wx.Panel):

    def __init__(self, parent):
        #wx.Panel.__init__(self, parent)
        #self.app = wx.App(False)
        self.d = {}
        self.parent = parent

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

        parent.SetSizer(box)
        parent.Layout()
        parent.Show()

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



"""
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="pyTable", size=(335, 252))
        designPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
"""