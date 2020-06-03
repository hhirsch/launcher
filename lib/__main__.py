import tkinter as tk
from tkinter import PhotoImage, Label, messagebox
from PIL import ImageTk, Image
import os, subprocess
from os import path
import json, math
from helper import *
from uihelper import *
from ui.launcherwindow import LauncherWindow
from sys import platform

root = tk.Tk()
launcherWindow = LauncherWindow(root)
cache = False;
json_file = 'launcher.json'
with open(json_file) as json_data:
    data = json.load(json_data)

rowLength = 4
if "launcher" in data:
    if "cache" in data["launcher"]:
        cache = (data["launcher"]["cache"] == "True")
    if "rowLength" in data["launcher"]:
        rowLength = data["launcher"]["rowLength"]
createWindowMenu(root, data)
currentColumn = 1;
for index, content in enumerate(data['games']):
    gameButton = addGame(root, content, data['games'][content])
    rawRow = (index+1) / rowLength
    currentRow = math.ceil(rawRow)
    root.rowconfigure(currentRow, weight=5)
    gameButton.grid(row=int(currentRow), column=currentColumn)
    if currentColumn == rowLength:
        currentColumn = 0;
    currentColumn += 1;
root.mainloop()
