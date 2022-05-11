import wx
import os
import glob

class projectFiles(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.filesTree = wx.TreeCtrl(parent, wx.ID_ANY, wx.DefaultPosition, (100, 70), wx.TR_HAS_BUTTONS | wx.TR_SINGLE | wx.TR_LINES_AT_ROOT)
        self.filesTree.Create
        root_path = "/Users/marek/PycharmProjects/pythonIDE"
        self.root = self.filesTree.AddRoot(root_path)

        #self.filesTree.AppendItem(itm, "Sub Item")
        self.filesTree.Expand(self.root)
        self.scanDir(root_path+"/*", self.root)

    def scanDir(self, dir, obj):
        txtfiles = []
        for file in glob.glob(dir):
            if os.path.isdir(file):
                subobj = self.filesTree.AppendItem(obj, ": "+os.path.basename(file))
                print("KAT "+os.path.basename(file))
                self.scanDir(file+"/*", subobj)
            else:
                print(os.path.basename(file))
                subobj = self.filesTree.AppendItem(obj, " - "+os.path.basename(file))
        return obj
