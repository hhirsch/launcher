from tkinter import Grid, N, W, S, E, messagebox
import math
from ui.launcherwindow import LauncherWindow
from config import Config
import os

config = Config()
try:
    config.load("launcher.json")
except:
    ERROR_MESSAGE_TITLE = "Config file not found"
    ERROR_MESSAGE_TEXT = "You don't have a launcher.json in your main directory."
    messagebox.showerror(title=ERROR_MESSAGE_TITLE, message=ERROR_MESSAGE_TEXT)
    quit()

launcherWindow = LauncherWindow()
cache = False;

try:
    cache = config.getValue(["launcher", "cache"])  == "True"
except:
    cache = False;

try:
    rowLength = config.getValue(["launcher", "rowLength"])
except:
    rowLength = 4

launcherWindow.createMenu(config.getValue(["launcher", "menu"]))
currentColumn = 1;


parentDir = 'games'
index = 0
for dirItem in os.listdir(parentDir):
    if os.path.isdir(os.path.join(parentDir, dirItem)):
        configFilePath = os.path.normpath(parentDir + '/' + dirItem + '/launcher.json')
        if os.path.exists(configFilePath):
            gameConfig = Config()
            try:
                gameConfig.load(configFilePath)
                gameButton = launcherWindow.getAppButton(dirItem, gameConfig)
                rawRow = (index+1) / rowLength
                currentRow = math.ceil(rawRow)
                launcherWindow.frame.rowconfigure(currentRow)
                Grid.rowconfigure(launcherWindow.frame, currentRow)
                gameButton.grid(row=int(currentRow), column=currentColumn, sticky=N+S+E+W)
                if currentColumn == rowLength:
                    currentColumn = 0;
                currentColumn += 1;
                index += 1
            except Exception as e:
                print(e)
                print("Problem loading")
                pass

launcherWindow.mainloop()
