import wx
from coolcalc.gui import MainWindow

app = wx.App(False)
frame = MainWindow(None, "Calculator")
app.MainLoop()