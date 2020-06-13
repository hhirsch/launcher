import tkinter as tk
from tkinter import Label, messagebox, ttk
from PIL import ImageTk, Image
from helper import getImagePath, gameIsInCache
from assetexception import AssetException
from callhelper import runGenericGame, runGenericGameWithStartup, runCommand
from sys import platform

def getRunFunction(game, data):
    if "startup" in data:
        runFunction = lambda: runGenericGameWithStartup(game, data)
    else:
        runFunction = lambda: runGenericGame(game, data)
    return runFunction


def getMenuRunFunction(path, data):
    runFunction = lambda: runCommand(path, data)
    return runFunction

def createButton(root, game, data):
    runFunction = getRunFunction(game, data)
    image = Image.open(getImagePath(game)).convert('RGBA')
    if not gameIsInCache(game):
        downloadIconImage = Image.open(getImagePath("download"))
        image.paste(downloadIconImage)
    gameImage = ImageTk.PhotoImage(image)
    gameButton = tk.Button(root, text=game, image=gameImage, command=runFunction, borderwidth=0)
    gameButton.image = gameImage

    return gameButton

def createButtonWithoutImage(root, game, data):
    runFunction = getRunFunction(game, data)
    invisiblePixel = tk.PhotoImage(width=1, height=1)
    gameButton = ttk.Button(root, text=game, image=invisiblePixel, command=runFunction, height = 215-10, width = 460-10, compound="c", borderwidth=0)
    gameButton.image = invisiblePixel

    return gameButton

def createMenu(root, game, menuData):
    menu = tk.Menu(root, tearoff=0)
    for index, content in enumerate(menuData):
        runFunction = getRunFunction(game, menuData[content])
        menu.add_command(label=content, command=runFunction)
    menu.add_command(label='close')

    return menu;

def showAbout():
    messagebox.showinfo("About", "Game Launcher made 2020 by Henry & Josepha Hirsch")

def createWindowMenu(root, menuData):
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    helpmenu = tk.Menu(menubar, tearoff=0)
    for index, content in enumerate(menuData):
        menuRunFunction = getMenuRunFunction("./", menuData[content])
        filemenu.add_command(label=content, command=menuRunFunction)

    filemenu.add_command(label="Quit", command=root.destroy)
    helpmenu.add_command(label="About", command=showAbout)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)
