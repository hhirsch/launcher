import tkinter as tk
from tkinter import PhotoImage, Label
from PIL import ImageTk, Image
import os, subprocess
from sys import platform
from os import path
import json
from lib import helper
from lib.assetexception import AssetException

def gameIsInProfile(game):
    return path.exists(helper.getProfilePath(game))

def gameIsInCache(game):
    return path.exists(helper.getCachePath(game))

def runGenericGame(game, data):
    gamePath = os.path.normpath(helper.getCachePath(game))
    if "path" in data:
        gamePath = gamePath + '/' + data['path']

    if "linux-exe" in data:
        call = [data['linux-exe']]
    else:
        call = data['exe']
        if platform in ["linux", "linux2"]:
            call.insert(0, "wine")

    if "params" in data:
        for index, param in enumerate(data['params']):
            call.append(param)

    subprocess.call(call, cwd=gamePath)

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

json_file = 'launcher.json'
with open(json_file) as json_data:
    data = json.load(json_data)

for index, content in enumerate(data['games']):
    gameButton = addGame(content, data['games'][content], root)
    currentRow = (index+1) / 5
    gameButton.grid(row=int(currentRow), column=index+1)

root.mainloop()
