from tkinter import *
import tkinter as tk
from tkinter import ttk
import math
from uihelper import createWindowMenu, createButton, createButtonWithoutImage
from ui.launcherwindow import LauncherWindow
from ui.detailwindow import DetailWindow
from ui.scrolledwindow import ScrolledWindow
from config import Config
from assetexception import AssetException

def addGame(root, game, config):
    data = config.getData()
    try:
        gameButton = createButton(root, game, data)
    except AssetException:
        gameButton = createButtonWithoutImage(root, game, data)

    gameButton.showDetail = lambda event: DetailWindow(root, game, config)
    gameButton.bind("<Button-3>", gameButton.showDetail)

    return gameButton

root = tk.Tk()

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

scrolledWindow = ScrolledWindow(root)
frame=Frame(scrolledWindow.scrollwindow)
frame.grid(row=0, column=0, sticky=N+S+E+W)

launcherWindow = LauncherWindow(root)
cache = False;

config = Config()
config.load("launcher.json")

try:
    cache = config.getValue(["launcher", "cache"])  == "True"
except:
    cache = False;

try:
    rowLength = config.getValue(["launcher", "rowLength"])
except:
    rowLength = 4

createWindowMenu(root, config.getValue(["launcher", "menu"]))
currentColumn = 1;
for index, content in enumerate(config.getValue(["games"])):
    gameButton = addGame(frame, content, config.getConfig(["games", content]))
    rawRow = (index+1) / rowLength
    currentRow = math.ceil(rawRow)
    frame.rowconfigure(currentRow)
    Grid.rowconfigure(frame, currentRow)
    gameButton.grid(row=int(currentRow), column=currentColumn, sticky=N+S+E+W)
    if currentColumn == rowLength:
        currentColumn = 0;
    currentColumn += 1;
root.mainloop()
