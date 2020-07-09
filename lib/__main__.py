from tkinter import Grid, N, W, S, E, messagebox
import math
from ui.launcherwindow import LauncherWindow
from config import Config
import os
from main import Main

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

parentDir = 'games'
main = Main(rowLength, launcherWindow)
for dirItem in os.listdir(parentDir):
    main.loadApp(parentDir, dirItem)
launcherWindow.mainloop()
