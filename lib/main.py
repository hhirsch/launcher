from tkinter import Grid, N, W, S, E, messagebox
import math
from ui.launcherwindow import LauncherWindow
from config import Config
import os

class Main:
    def __init__(self, rowLength, launcherWindow):
        self.currentColumn = 1;
        self.index = 0
        self.rowLength = rowLength
        self.launcherWindow = launcherWindow
    def loadApp(self, parentDir, dirItem):
        if os.path.isdir(os.path.join(parentDir, dirItem)):
            configFilePath = os.path.normpath(parentDir + '/' + dirItem + '/launcher.json')
            if os.path.exists(configFilePath):
                gameConfig = Config()
                try:
                    gameConfig.load(configFilePath)
                    gameButton = self.launcherWindow.getAppButton(dirItem, gameConfig)
                    rawRow = (self.index+1) / self.rowLength
                    currentRow = math.ceil(rawRow)
                    self.launcherWindow.frame.rowconfigure(currentRow)
                    Grid.rowconfigure(self.launcherWindow.frame, currentRow)
                    gameButton.grid(row=int(currentRow), column=self.currentColumn, sticky=N+S+E+W)
                    if self.currentColumn == self.rowLength:
                        self.currentColumn = 0;
                    self.currentColumn += 1;
                    self.index += 1
                except Exception as e:
                    print(e)
                    print("Problem loading")
                    pass
