import tkinter as tk
from tkinter import Label, ttk
from helper import getImagePath, gameIsInCache
from uihelper import getRunFunction, getImageOrException
from assetexception import AssetException

class DetailWindow:
    def __init__(self, root, game, config):
        self.currentRow = 0
        self.root = root
        self.window = tk.Toplevel(root)
        self.window.title("Game Launcher " + game)
        self.window.geometry("460x800")
        self.window.resizable(0, 0)
        try:
            appTitle = config.getValue(["title"])
        except:
            appTitle = game

        gameName = Label(self.window, text=appTitle)
        self._addWidget(gameName)
        gameName.config(font=("Sans", 20))
        try:
            self.window.gameImage = getImageOrException(game)
            panel = ttk.Label(self.window, image = self.window.gameImage)
        except AssetException:
            invisiblePixel = tk.PhotoImage(width=460, height=1)
            self.window.gameImage = invisiblePixel
            panel = ttk.Label(self.window, image = self.window.gameImage)
        self._addWidget(panel)
        try:
            appDescription = config.getValue(["description"])
            gameDescription = Label(self.window, text=appDescription)
            self._addWidget(gameDescription)
        except:
            pass

        self._createButtons(root, game, config.getData())

    def _addWidget(self, widget):
        widget.grid(column=0,row=self.currentRow, sticky='nesw')
        self.currentRow += 1
    def _createButtons(self, root, game, data):
        runFunction = getRunFunction(game, data)
        button = ttk.Button(self.window, text="Play", command=runFunction)
        self._addWidget(button)

        if "menu" in data:
            menuData = data['menu']
            for index, content in enumerate(menuData):
                if "title" in menuData[content]:
                    itemTitle = Label(self.window)
                    itemTitle.config(font=("Sans", 15))
                    self._addWidget(itemTitle)
                    itemTitle = Label(self.window, text=menuData[content]["title"])
                    itemTitle.config(font=("Sans", 15))
                    self._addWidget(itemTitle)
                runFunction = getRunFunction(game, menuData[content])
                button = ttk.Button(self.window, text=content, command=runFunction)
                self._addWidget(button)
                if "description" in menuData[content]:
                    itemDescription = Label(self.window, text=menuData[content]["description"])
                    self._addWidget(itemDescription)
