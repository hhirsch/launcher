import tkinter as tk
from tkinter import Label, messagebox, ttk, Button
from PIL import ImageTk, Image
from helper import getImagePath, gameIsInCache
from uihelper import getRunFunction
from config import Config

class DetailWindow:
    def __init__(self, root, game, config):
        self.currentRow = 0
        self.root = root
        self.window = tk.Toplevel(root)
        self.window.title("Game Launcher " + game)
        self.window.geometry("460x600")
        self.window.resizable(0, 0)
        try:
            appTitle = config.getValue(["title"])
        except:
            appTitle = game

        gameName = Label(self.window, text=appTitle)
        self._addWidget(gameName)
        gameName.config(font=("Sans", 20))
        image = Image.open(getImagePath(game)).convert('RGBA')
        if not gameIsInCache(game):
            downloadIconImage = Image.open(getImagePath("download"))
            image.paste(downloadIconImage)
        self.window.gameImage = ImageTk.PhotoImage(image)
        panel = tk.Label(self.window, image = self.window.gameImage)
        self._addWidget(panel)
        self._createButtons(root, game, config.getData())

    def _addWidget(self, widget):
        widget.grid(column=0,row=self.currentRow, sticky='nesw')
        self.currentRow += 1
    def _createButtons(self, root, game, data):
        runFunction = getRunFunction(game, data)
        button = tk.Button(self.window, text="Play", command=runFunction)
        self._addWidget(button)

        if "menu" in data:
            menuData = data['menu']
            for index, content in enumerate(menuData):
                runFunction = getRunFunction(game, menuData[content])
                button = tk.Button(self.window, text=content, command=runFunction)
                self._addWidget(button)
