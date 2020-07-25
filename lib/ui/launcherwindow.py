from tkinter import Tk, Grid, Frame, N, S, E, W, Menu, messagebox, font
from ui.scrolledwindow import ScrolledWindow
from uihelper import createButton, createButtonWithoutImage
from assetexception import AssetException
from callhelper import runCommand
from ui.detailwindow import DetailWindow
from ui.color import Color
from ui.launchermenu import LauncherMenu

class LauncherWindow:
    def __init__(self, serviceLocator):
        self.serviceLocator = serviceLocator
        self.root = serviceLocator.root
        self.menu = LauncherMenu(serviceLocator)
        self.root.title("Game Launcher")
        Grid.rowconfigure(self.root, 0, weight=1)
        Grid.columnconfigure(self.root, 0, weight=1)
        scrolledWindow = ScrolledWindow(self.root)
        self.frame=Frame(scrolledWindow.scrollwindow, bg = Color.background)
        self.frame.grid(row=0, column=0, sticky=N+S+E+W)
    def mainloop(self):
        self.root.mainloop()
    def getAppButton(self, game, config):
        data = config.getData()
        try:
            gameButton = createButton(self.frame, game, data)
        except AssetException:
            gameButton = createButtonWithoutImage(self.frame, game, data)

        gameButton.showDetail = lambda event: DetailWindow(self.frame, game, config, self.serviceLocator)
        gameButton.bind("<Button-3>", gameButton.showDetail)

        return gameButton
    def createMenu(self, menuData):
        self.menu.createMenu(menuData)
