import tkinter as tk
from tkinter import Label, ttk, CENTER, NW, StringVar, OptionMenu, NORMAL, DISABLED
from helper import getImagePath, gameIsInCache
from uihelper import getRunFunction, getImageOrException, removeBorders
from runnerfactory import RunnerFactory
from assetexception import AssetException
from ui.color import Color
from ui.style import Style
from ui.settingwindow import SettingWindow
from queue import Queue
from threading import Thread
from concurrent import futures

class DetailWindow:
    def __init__(self, root, game, config, serviceLocator):
        self.game = game
        self.columnSpan = 4
        self.currentRow = 0
        self.root = root
        self.window = tk.Toplevel(root, bg=Color.darkBackground)
        self.window.title("Game Launcher " + game)
        self.window.geometry("460x470")
        self.window.resizable(0, 0)
        config.setValue("appName", game)
        self.config = config
        self.serviceLocator = serviceLocator
        self.runner = RunnerFactory.getRunner(self.config)
        try:
            appTitle = config.getValue(["title"])
        except:
            appTitle = game

        gameName = Label(self.window, text=appTitle)
        Color.paintDark(gameName)
        self._addWidgetFullWidth(gameName)
        gameName.config(font=("Impact", 20))
        try:
            self.window.gameImage = getImageOrException(game)
            panel = tk.Label(self.window, image = self.window.gameImage)
        except AssetException:
            invisiblePixel = tk.PhotoImage(width=460, height=1)
            self.window.gameImage = invisiblePixel
            panel = tk.Label(self.window, image = self.window.gameImage)
        Color.paint(panel)
        panel.grid(column=0,row=self.currentRow, sticky='ns', columnspan=self.columnSpan)
        self.currentRow += 1

        try:
            appDescription = config.getValue(["description"])
            gameDescription = Label(self.window, heigh=5, text=appDescription)
            Color.paintBox(gameDescription)
            gameDescription.config(relief='flat', borderwidth=20)
            self._addWidgetFullWidth(gameDescription)
        except:
            pass
        self._createPlayButton()
        self._createTopBarButtons(self.window, game, config.getData())

        try:
            appTitle = config.getValue(["mods"])
            self._createModSelector(self.window, config.getData())
            self.currentRow += 1
        except:
            self._createEmptyModSelector(self.window, config.getData())
            self.currentRow += 1
        self.currentRow += 1
        self._createFooterButtons(self.window)
        self.currentRow += 1
    def _addWidget(self, widget):
        widget.grid(column=0,row=self.currentRow, sticky='ns', columnspan=self.columnSpan)
        self.currentRow += 1
    def _addWidgetFullWidth(self, widget):
        widget.grid(column=0,row=self.currentRow, sticky='nswe', columnspan=self.columnSpan)
        self.currentRow += 1
    def _runAndLog(self):
        result = self.runner.run()
        self.serviceLocator.systemWindow.addMessage(result.stdout)
        self.serviceLocator.systemWindow.addMessage(result.stderr)
    def _runAndLogThread(self):
        self.playButton.configure(text="Running")
        self.playButton["state"] = DISABLED
        thread_pool_executor.submit(self._runAndLog)
        self.playButton["state"] = NORMAL
        self.playButton.configure(text="▶ Play")
    def _createPlayButton(self):
        self.playButtonText = tk.StringVar()
        self.playButtonText.set("▶ Play")
        playFunction = lambda: self._runAndLogThread()
        self.playButton = tk.Button(self.window, text="▶ Play", width=5, command=playFunction)
        removeBorders(self.playButton)
        Style.stylePrimaryButton(self.playButton)
        self.playButton.grid(rowspan=2, column=0,row=self.currentRow, sticky='nws')
    def _createModSelector(self, root, data):
        modLabel = Label(self.window)
        removeBorders(modLabel)
        Color.paintDark(modLabel)
        modLabel.grid(column=3,row=self.currentRow, sticky='nswe', columnspan=1)
        variable = StringVar(self.window)
        variable.set("Standard") # default value
        options = self.config.getValue(["mods"])
        option = OptionMenu(self.window, variable, *options , command=self.modSelected)
        option.config(relief='flat')
        removeBorders(option)
        Color.paintDark(option)
        Color.paintDark(option["menu"])
        option.grid(column=1,row=self.currentRow, sticky='nsw', columnspan=2)
    def _createEmptyModSelector(self, root, data):
        modLabel = Label(self.window)
        removeBorders(modLabel)
        Color.paintDark(modLabel)
        modLabel.grid(column=1,row=self.currentRow, sticky='nswe', columnspan=4)
    def modSelected(self, value):
        modConfig = self.config.getConfig(["mods", value])
        modConfig.setValue("appName", self.game)
        newRunner = RunnerFactory.getRunner(self.config)
        self.runner = RunnerFactory.modifyRunner(newRunner, modConfig)
    def _createTopBarButtons(self, root, game, data):
        topBarColumn = 1
        if "top-bar" in data:
            topBarData = data['top-bar']
            for index, content in enumerate(topBarData):
                runFunction = getRunFunction(game, topBarData[content])
                button = tk.Button(self.window, text=content, command=runFunction)
                removeBorders(button)
                Style.styleButton(button)
                button.grid(column=topBarColumn,row=self.currentRow, sticky='nsw')
                topBarColumn += 1
        self.currentRow += 1
    def _createFooterButtons(self, root):
        modLabel = Label(self.window)
        removeBorders(modLabel)
        Color.paintDark(modLabel)
        modLabel.grid(column=0,row=self.currentRow, sticky='nswe', columnspan=4)
        self.currentRow += 1
        button = tk.Button(self.window, text="Savegame Config")
        removeBorders(button)
        Color.paintDark(button)
        button.grid(column=0,row=self.currentRow, sticky='sw')
        if self.config.hasValue("linux-tweaks"):
            linuxTweaks = lambda: SettingWindow(self.window, self.game, self.config)
            button = tk.Button(self.window, text="Linux Tweaks", command=linuxTweaks)
        else:
            button = tk.Button(self.window, text="Linux Tweaks")
        removeBorders(button)
        Color.paintDark(button)
        button.grid(column=1,row=self.currentRow, sticky='sw')
        button = tk.Button(self.window, text="Game Tools")
        removeBorders(button)
        Color.paintDark(button)
        button.grid(column=2,row=self.currentRow, sticky='sw')
        button = tk.Button(self.window, text="Game Info")
        removeBorders(button)
        Color.paintDark(button)
        button.grid(column=3,row=self.currentRow, sticky='sw')

    def _createButtons(self, root, game, data):
        if "detail" in data:
            detailData = data['detail']
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
