from tkinter import Tk, Grid, Frame, N, S, E, W, Menu, messagebox, font
from ui.scrolledwindow import ScrolledWindow
from uihelper import createButton, createButtonWithoutImage
from assetexception import AssetException
from callhelper import runCommand
from ui.detailwindow import DetailWindow
from ui.color import Color

class LauncherMenu:
    def __init__(self, root):
        self.root = root

    def getMenuRunFunction(self, path, data):
        runFunction = lambda: runCommand(path, data)
        return runFunction

    def showAbout(self):
        messagebox.showinfo("About", "Game Launcher made 2020 by Henry & Josepha Hirsch")

    def createMenu(self, menuData):
        menubar = Menu(self.root, relief='flat')
        Color.paintDark(menubar)
        filemenu = Menu(menubar, tearoff=0, relief='flat')
        Color.paintDark(filemenu)
        helpmenu = Menu(menubar, tearoff=0, relief='flat')
        Color.paintDark(helpmenu)
        for index, content in enumerate(menuData):
            menuRunFunction = self.getMenuRunFunction("./", menuData[content])
            filemenu.add_command(label=content, command=menuRunFunction)

        filemenu.add_command(label="Quit", command=self.root.destroy)
        helpmenu.add_command(label="About", command=self.showAbout)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Help", menu=helpmenu)
        menubar.add_command(label="System", command=self.showAbout)
        menubar.add_command(label="Network", command=self.showAbout)
        menubar.add_command(label="Profile", command=self.showAbout)
        self.root.config(menu=menubar)
