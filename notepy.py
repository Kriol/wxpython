__author__ = 'krio'

import wx
import os


class Window(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(640, 480))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

        menu = wx.Menu()
        open_item = menu.Append(wx.ID_OPEN, 'Open', 'Open file')
        about_item = menu.Append(wx.ID_ABOUT, 'About', 'About NotePy')
        exit_item = menu.Append(wx.ID_EXIT, 'Exit', 'Bye')

        bar = wx.MenuBar()
        bar.Append(menu, 'File')
        self.SetMenuBar(bar)
        self.Bind(wx.EVT_MENU, self.on_open, open_item)
        self.Bind(wx.EVT_MENU, self.on_about, about_item)
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)

    def on_open(self, e):
        self.dirname = ' '
        open_dlg = wx.FileDialog(self, 'Choose file', self.dirname, ' ', '*.*', wx.OPEN)
        if open_dlg.ShowModal() == wx.ID_OK:
            self.filename = open_dlg.GetFilename()
            self.dirname = open_dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
            wnd.SetTitle(self.filename + ' - NotePy')

    def on_about(self, e):
        about_dlg = wx.MessageDialog(self, 'any-body text', 'About NotePy', wx.OK)
        about_dlg.ShowModal()

    def on_exit(self, e):
        self.control.SetValue('Close me!')


app = wx.App()
wnd = Window(None, 'NotePy')
app.MainLoop()
