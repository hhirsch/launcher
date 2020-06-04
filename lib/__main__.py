import tkinter as tk
import math
from uihelper import createWindowMenu, addGame
from ui.launcherwindow import LauncherWindow
from config import Config

root = tk.Tk()
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
    gameButton = addGame(root, content, config.getValue(["games", content]))
    rawRow = (index+1) / rowLength
    currentRow = math.ceil(rawRow)
    root.rowconfigure(currentRow, weight=5)
    gameButton.grid(row=int(currentRow), column=currentColumn)
    if currentColumn == rowLength:
        currentColumn = 0;
    currentColumn += 1;
root.mainloop()
