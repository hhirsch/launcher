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

json_file = 'launcher.json'
with open(json_file) as json_data:
    data = json.load(json_data)

createWindowMenu(root, data)
currentColumn = 1;
rowLenght = 4
for index, content in enumerate(data['games']):
    gameButton = addGame(root, content, data['games'][content])
    rawRow = (index+1) / rowLenght
    currentRow = math.ceil(rawRow)
    root.rowconfigure(currentRow, weight=5)
    gameButton.grid(row=int(currentRow), column=currentColumn)
    if currentColumn == rowLenght:
        currentColumn = 0;
    currentColumn += 1;
root.mainloop()
