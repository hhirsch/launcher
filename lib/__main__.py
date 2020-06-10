from tkinter import *
import tkinter as tk
import math
from uihelper import createWindowMenu, addGame
from ui.launcherwindow import LauncherWindow
from ui.scrolledwindow import ScrolledWindow
from config import Config

root = tk.Tk()
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

scrolledWindow = ScrolledWindow(root)
frame=Frame(scrolledWindow.scrollwindow)
frame.grid(row=0, column=0, sticky=N+S+E+W)

launcherWindow = LauncherWindow(root)
cache = False;

config = Config("launcher.json")

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
    gameButton = addGame(frame, content, config.getValue(["games", content]))
    rawRow = (index+1) / rowLength
    currentRow = math.ceil(rawRow)
    frame.rowconfigure(currentRow, weight=1)
    Grid.rowconfigure(frame, currentRow, weight=1)
    gameButton.grid(row=int(currentRow), column=currentColumn, sticky=N+S+E+W)
    if currentColumn == rowLength:
        currentColumn = 0;
    currentColumn += 1;
root.mainloop()
