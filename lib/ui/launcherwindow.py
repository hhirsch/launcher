from tkinter import Tk, Grid, Frame, N, S, E, W, Menu, messagebox, font
from ui.scrolledwindow import ScrolledWindow
from uihelper import createButton, createButtonWithoutImage
from assetexception import AssetException
from callhelper import runCommand
from ui.detailwindow import DetailWindow
from ui.color import Color

class LauncherWindow:
    def __init__(self):
        root = Tk()
        self.root = root
        root.title("Game Launcher")
        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)
        scrolledWindow = ScrolledWindow(root)
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

        gameButton.showDetail = lambda event: DetailWindow(self.frame, game, config)
        gameButton.bind("<Button-3>", gameButton.showDetail)

        return gameButton

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
        self.root.config(menu=menubar)
