import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar() # create a menubar object
        fileMenu = wx.Menu() # create a menu object
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application') # name of the menu item, append menu item into the menu object
        menubar.Append(fileMenu, '&File') # append a menu into the menubar
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem) # bind the wx.EVT_MENU of the menu item

        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        self.Centre()

    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()