import wx
import os
import glob
from pubsub import pub

class projectFiles(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.filesTree = wx.TreeCtrl(parent, wx.ID_ANY, wx.DefaultPosition, (100, 70), wx.TR_HAS_BUTTONS | wx.TR_SINGLE | wx.TR_LINES_AT_ROOT)
        self.filesTree.Create
        root_path = "/Users/marek/PycharmProjects/pythonIDE"
        self.root = self.filesTree.AddRoot(root_path)

        #self.filesTree.AppendItem(itm, "Sub Item")
        self.scanDir(root_path+"/*", self.root)
        self.filesTree.Expand(self.root)
        self.filesTree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self._click)

    def _click(self, event):
        item = event.GetItem()
        label = self.filesTree.GetItemText(item)

        path = ""

        while self.filesTree.GetItemParent(item):
            piece = self.filesTree.GetItemText(item)
            path = piece[3:] + "/" + path
            item = self.filesTree.GetItemParent(item)

        #piece = self.filesTree.GetItemText(item)
        path = self.filesTree.GetItemText(item)+"/"+path[0:-1]

        pub.sendMessage("openTabFile", message=path)
        print("Run handler (openTabFile) = "+label)

    def scanDir(self, dir, obj):
        txtfiles = []
        for file in glob.glob(dir):
            if os.path.isdir(file):
                subobj = self.filesTree.AppendItem(obj, " : "+os.path.basename(file))
                #print("KAT "+os.path.basename(file))
                self.scanDir(file+"/*", subobj)
            else:
                #print(os.path.basename(file))
                subobj = self.filesTree.AppendItem(obj, " - "+os.path.basename(file))
        return obj

