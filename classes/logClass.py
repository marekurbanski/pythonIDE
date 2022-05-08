import wx
from pubsub import pub

class log():

    def __init__(self):
        print("Debugger started")

    def Debug(self, info):
        print(info)
        pub.sendMessage("add_log", message="Debug: "+info)


    def Info(self, info):
        print(info)

    def Error(self, info):
        print(info)