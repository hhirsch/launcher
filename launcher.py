import tkinter as tk
from tkinter import PhotoImage, Label
from PIL import ImageTk, Image
import os, subprocess
from sys import platform
from os import path
import json

def getImagePath(game):
    imagePath = os.path.normpath('data/images/' + game)
    if path.exists(imagePath + '.png'):
        return imagePath + '.png'

    if path.exists(imagePath + '.jpg'):
        return imagePath + '.jpg'

def getCachePath(game):
    return os.path.normpath('repository/' + game)

def getProfilePath(game):
    return os.path.normpath('games/' + game)

def gameIsInProfile(game):
    return path.exists(getProfilePath(game))

def gameIsInCache(game):
    return path.exists(getCachePath(game))


def copyToProfile(game):
    print('hello')


def runGenericGame(game, data):
    gamePath = os.path.normpath(getCachePath(game))
    if data['path']:
        gamePath = gamePath + '/' + data['path']

    exePath = data['exe']
    call = [exePath]

    if platform in ["linux", "linux2"]:
        call.insert(0, "wine")

    if data['params']:
        for index, param in enumerate(data['params']):
            call.append(param)


    subprocess.call(call, cwd=gamePath)


def getRunFunction(game, data):
    runFunction = lambda: runGenericGame(game, data)
    return runFunction


def addGame(game, data, root):
    runFunction = getRunFunction(game, data)
    gameImage = ImageTk.PhotoImage(Image.open(getImagePath(game)))
    label = Label(image=gameImage)
    label.image = gameImage
    gameButton = tk.Button(root, text=game, image=gameImage, command=runFunction)
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
