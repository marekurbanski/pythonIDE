import wx
import os.path
from classes import logClass
from xml.dom import minidom
import xml.etree.ElementTree as ET


class settings(wx.Frame):

    global filename
    filename = "settings.xml"

    def __init__(self, mainIDE):
        print("OK")



    def get(self, path, attr):
        if os.path.exists(filename):
            logClass.log.Debug(self, "Config file exists")
            datasource = open(filename)
            try:
                tree = ET.parse(filename)
                root = tree.getroot()
                #mydoc = minidom.parse(datasource)
                mainWindow = ET.SubElement(root, 'mainWindow')
                mainWindow_width = ET.SubElement(mainWindow, 'width')
                #mainWindow_width = mainWindow.getElementsByTagName('width')
                #print(mainWindow.attrib)
                #print(root.find('./'+path).text)
                val = (root.find('./'+path).attrib.get(attr))
                #print(mainWindow_width.attrib.get("value"))
                return val
            except:
                logClass.log.Error(self,"Error config file - no valid XML")

        else:
            logClass.log.Info(self, "No config file", filename)
