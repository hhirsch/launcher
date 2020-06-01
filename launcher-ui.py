import tkinter as tk
from tkinter import PhotoImage, Label, messagebox
from PIL import ImageTk, Image
import os, subprocess
from os import path
import json
from lib import helper
from lib.assetexception import AssetException
from lib.callhelper import runGenericGame

def getRunFunction(game, data):
    runFunction = lambda: runGenericGame(game, data)
    return runFunction

def addGame(game, data, root):
    runFunction = getRunFunction(game, data)
    try:
        gameImage = ImageTk.PhotoImage(Image.open(helper.getImagePath(game)))
        label = Label(image=gameImage)
        label.image = gameImage
        gameButton = tk.Button(root, text=game, image=gameImage, command=runFunction)
    except AssetException:
        invisiblePixel = tk.PhotoImage(width=1, height=1)
        label = Label(image=invisiblePixel)
        label.image = invisiblePixel
        gameButton = tk.Button(root, text=game, image=invisiblePixel, command=runFunction, height = 206-10, width = 390-10, compound="c")
    return gameButton

root = tk.Tk()
root.geometry("960x600")
root.title('Game Launcher')

json_file = 'launcher.json'
with open(json_file) as json_data:
    data = json.load(json_data)

def showAbout():
    messagebox.showinfo("About", "Game Launcher made 2020 by Henry & Josepha Hirsch")

def createMenu(root):
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label='about', command=showAbout)
    menu.add_command(label='close')

    return menu;

for index, content in enumerate(data['games']):
    gameButton = addGame(content, data['games'][content], root)
    currentRow = (index+1) / 5
    menu = createMenu(root)
    showMenu = lambda event: menu.post(event.x_root, event.y_root)
    gameButton.bind("<Button-3>", showMenu)
    gameButton.grid(row=int(currentRow), column=index+1)

root.mainloop()
