from tkinter import Grid, N, W, S, E, messagebox
import math
from ui.launcherwindow import LauncherWindow
from config import Config
import os
from main import Main

config = Config()
try:
    config.load(os.path.join(os.getcwd(),"launcher.json"))
except:
    ERROR_MESSAGE_TITLE = "Config file not found"
    ERROR_MESSAGE_TEXT = "You don't have a launcher.json in your main directory."
    messagebox.showerror(title=ERROR_MESSAGE_TITLE, message=ERROR_MESSAGE_TEXT)
    quit()


cache = False;

try:
    cache = config.getValue(["launcher", "cache"])  == "True"
except:
    cache = False;

try:
    rowLength = config.getValue(["launcher", "rowLength"])
except:
    rowLength = 4

repositoryDirectory = 'games'
main = Main(rowLength, config)
for applicationDirectory in os.listdir(repositoryDirectory):
    main.loadApp(repositoryDirectory, applicationDirectory)
main.run()
