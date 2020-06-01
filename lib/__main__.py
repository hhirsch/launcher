import tkinter as tk
from tkinter import PhotoImage, Label, messagebox
from PIL import ImageTk, Image
import os, subprocess
from os import path
import json, math
from helper import *
from uihelper import *
from callhelper import runGenericGame
from sys import platform

root = tk.Tk()
root.geometry("960x600")
root.title('Game Launcher')

json_file = 'launcher.json'
with open(json_file) as json_data:
    data = json.load(json_data)

createWindowMenu(root, data)
currentColumn = 1;
rowLenght = 4
for index, content in enumerate(data['games']):
    gameButton = addGame(content, data['games'][content], root)
    rawRow = (index+1) / rowLenght
    currentRow = math.ceil(rawRow)
    if "menu" in data['games'][content]:
        menu = createMenu(root, content, data['games'][content]['menu'])
        showMenu = lambda event: menu.post(event.x_root, event.y_root)
        gameButton.bind("<Button-3>", showMenu)

    gameButton.grid(row=int(currentRow), column=currentColumn)
    if currentColumn == rowLenght:
        currentColumn = 0;
    currentColumn += 1;
root.mainloop()
