import wx

class Input_Panel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        # Input variables
        self.tittle1 = wx.StaticText(self, label="Inputs:")
        self.lblname1 = wx.StaticText(self, label="Input 1:")
        self.format1 = ['Option 1','Option 2']
        self.combo1 = wx.ComboBox(self, size=(200, -1),value='', choices=self.format1, style=wx.CB_DROPDOWN)
        self.lblname2 = wx.StaticText(self, label="Input 2")
        self.format2 = ['Option 1','Option 2', 'Option 3']
        self.combo2 = wx.ComboBox(self, size=(200, -1),value='', choices=self.format2, style=wx.CB_DROPDOWN)

        # Set sizer for the panel content
        self.sizer = wx.GridBagSizer(2, 2)
        self.sizer.Add(self.tittle1, (1, 2))
        self.sizer.Add(self.lblname1, (2, 1))
        self.sizer.Add(self.combo1, (2, 2))
        self.sizer.Add(self.lblname2, (3, 1))
        self.sizer.Add(self.combo2, (3, 2))
        self.SetSizer(self.sizer)

class Output_Panel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        # Output variables
        self.tittle2 = wx.StaticText(self, label="Outputs:")
        self.lblname3 = wx.StaticText(self, label="Output1")
        self.result3 = wx.StaticText(self, label="", size=(100, -1))

        # Set sizer for the panel content
        self.sizer = wx.GridBagSizer(2, 2)
        self.sizer.Add(self.tittle2, (1, 2))
        self.sizer.Add(self.lblname3, (2, 1))
        self.sizer.Add(self.result3, (2, 2))
        self.SetSizer(self.sizer)

class Main_Window(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title)

        # Set variable panels
        self.splitter = wx.SplitterWindow(self)
        self.panel1 = Input_Panel(self.splitter)
        self.panel2 = Output_Panel(self.splitter)
        self.splitter.SplitVertically(self.panel1, self.panel2)

        self.windowSizer = wx.BoxSizer(wx.VERTICAL)
        self.windowSizer.Add(self.splitter, 1, wx.ALL | wx.EXPAND)
        self.SetSizerAndFit(self.windowSizer)

def main():
    app = wx.App(False)
    frame = Main_Window(None, "App GUI")
    frame.Show()
    app.MainLoop()

if __name__ == "__main__" :
    main()