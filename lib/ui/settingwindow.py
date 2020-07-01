import tkinter as tk
from tkinter import Label, ttk, CENTER, NW, StringVar, OptionMenu
from helper import getImagePath, gameIsInCache
from uihelper import getRunFunction, getImageOrException, removeBorders
from assetexception import AssetException
from ui.color import Color
from ui.style import Style
from callhelper import runCommand

class SettingWindow:
    def __init__(self, root, game, config):
        self.currentRow = 0
        self.window = tk.Toplevel(root, bg=Color.background)
        self.window.title("Linux Tweaks")
        self.window.geometry("350x900")
        self.window.resizable(0, 0)
        self._createButtons(root, game, config.getData())
    def _createButtons(self, root, game, data):
        if "linux-tweaks" in data:
            detailData = data['linux-tweaks']
            for index, content in enumerate(detailData):
                if "title" in detailData[content]:
                    spaceItem = Label(self.window)
                    spaceItem.config(font=("Impact", 15))
                    Color.paint(spaceItem)
                    self._addWidget(spaceItem)
                    itemTitle = Label(self.window, text=detailData[content]["title"])
                    Color.paint(itemTitle)
                    itemTitle.config(font=("Impact", 15))
                    self._addWidget(itemTitle)
                runFunction = getRunFunction(game, detailData[content])
                button = tk.Button(self.window, text=content, command=runFunction)
                removeBorders(button)
                Style.styleButton(button)
                self._addWidget(button)
                if "description" in detailData[content]:
                    itemDescription = Label(self.window, text=detailData[content]["description"])
                    Color.paint(itemDescription)
                    self._addWidget(itemDescription)

    def _addWidget(self, widget):
        widget.grid(column=0,row=self.currentRow, sticky='ns')
        self.currentRow += 1
    def _addWidgetFullWidth(self, widget):
        widget.grid(column=0,row=self.currentRow, sticky='nswe')
        self.currentRow += 1
