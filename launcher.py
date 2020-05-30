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

def runAoe():
    game = "wololo-kingdoms"
    if not gameIsInProfile(game):
        copyToProfile(game)
    agePath = os.path.normpath('wololo-kingdoms/age2_x1')
    if platform in ["linux", "linux2"]:
        subprocess.call(["wine", "WK.exe"], cwd=agePath)
    else:
        subprocess.call("WK.exe", cwd=agePath)


def runAnno():
    agePath = os.path.normpath('anno')
    if platform in ["linux", "linux2"]:
        subprocess.call(["wine", "1602.exe"], cwd=agePath)
    else:
        subprocess.call("1602.exe", cwd=agePath)
    print('hello')

def runGenericGame(game, data):
    gamePath = os.path.normpath(getCachePath(game))
    if data['path']:
        gamePath = gamePath + '/' + data['path']
    print(gamePath)
    exePath = data['exe']
    if platform in ["linux", "linux2"]:
        subprocess.call(["wine", exePath], cwd=gamePath)
    else:
        subprocess.call(exePath, cwd=gamePath)
    print('hello')

def getRunFunction(game, data):
    runFunction = lambda: runGenericGame(game, data)
    return runFunction


def addGame(game, data, root):
    runFunction = getRunFunction(game, data)
    gameImage = ImageTk.PhotoImage(Image.open(getImagePath(game)))
    label = Label(image=gameImage)
    label.image = gameImage # keep a reference!
    print(gameImage)
    gameButton = tk.Button(root, text=game, image=gameImage, command=runFunction)
    return gameButton

root = tk.Tk()
root.geometry("960x600")

json_file = 'launcher.json'
with open(json_file) as json_data:
    data = json.load(json_data)

#for i in range(len(data['games'])):
#    print (games[i])
for index, content in enumerate(data['games']):
    gameButton = addGame(content, data['games'][content], root)
    currentRow = (index+1) / 5
    gameButton.grid(row=int(currentRow), column=index+1)
#    print(content, data['games'][content])

# annoImg = ImageTk.PhotoImage(Image.open(os.path.normpath("data/anno.jpg")))
# aoeImg = ImageTk.PhotoImage(Image.open(os.path.normpath("data/wololo-kingdoms.png")))

# annoButton = tk.Button(root, text="anno", image=annoImg, command=runAnno)
# annoButton.grid(row=1,column=1)

# aoeButton = tk.Button(root, text="age", image=aoeImg, command=runAoe)
# aoeButton.grid(row=1,column=2)

root.mainloop()
