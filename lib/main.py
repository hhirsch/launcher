from tkinter import Grid, N, W, S, E, messagebox
import math
from ui.launcherwindow import LauncherWindow
from config import Config
from servicelocatorfactory import ServiceLocatorFactory
import os

class Main:
    def __init__(self, queue, rowLength, config):
        self.currentColumn = 1;
        self.index = 0
        self.rowLength = rowLength
        serviceLocator = ServiceLocatorFactory.getServiceLocator(config)
        launcherWindow = LauncherWindow(serviceLocator)
        launcherWindow.createMenu(config.getValue(["launcher", "menu"]))
        self.launcherWindow = launcherWindow
    def initializeServices():
        pass
    def run(self):
        self.launcherWindow.mainloop()
    def loadApp(self, repositoryDirectory, appDirectory):
        if os.path.isdir(os.path.join(repositoryDirectory, appDirectory)):
            configFilePath = os.path.normpath(repositoryDirectory + '/' + appDirectory + '/launcher.json')
            if os.path.exists(configFilePath):
                gameConfig = Config()
                try:
                    gameConfig.load(configFilePath)
                    gameButton = self.launcherWindow.getAppButton(appDirectory, gameConfig)
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
                    print("Problem loading")
                    print(e)
                    pass
