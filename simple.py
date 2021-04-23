import wx

app = wx.App() # application object

frame = wx.Frame(None, title = "Simple application") # wx.frame object, parent widget for other widget
frame.Show() # display it on the screen

app.MainLoop() # endless cycle