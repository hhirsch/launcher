import tkinter as tk
from tkinter import Label, messagebox
from PIL import ImageTk, Image
from helper import getImagePath, gameIsInCache
from assetexception import AssetException
from callhelper import runGenericGame, runGenericGameWithStartup
from sys import platform

def getRunFunction(game, data):
    if "startup" in data:
        runFunction = lambda: runGenericGameWithStartup(game, data)
    else:
        runFunction = lambda: runGenericGame(game, data)
    return runFunction

def createButton(root, game, data):
    runFunction = getRunFunction(game, data)
    image = Image.open(getImagePath(game)).convert('RGBA')
    if not gameIsInCache(game):
        downloadIconImage = Image.open(getImagePath("download"))
        image.paste(downloadIconImage)
    gameImage = ImageTk.PhotoImage(image)
    label = Label(image=gameImage)
    label.image = gameImage
    gameButton = tk.Button(root, text=game, image=gameImage, command=runFunction, borderwidth=0)

    return gameButton

def createButtonWithoutImage(root, game, data):
    runFunction = getRunFunction(game, data)
    invisiblePixel = tk.PhotoImage(width=1, height=1)
    label = Label(image=invisiblePixel)
    label.image = invisiblePixel
    gameButton = tk.Button(root, text=game, image=invisiblePixel, command=runFunction, height = 215-10, width = 460-10, compound="c", borderwidth=0)

    return gameButton

def addGame(root, game, data):
    try:
        gameButton = createButton(root, game, data)
    except AssetException:
        gameButton = createButtonWithoutImage(root, game, data)
    if "menu" in data:
        menu = createMenu(root, game, data['menu'])
        showMenu = lambda event: menu.post(event.x_root, event.y_root)
        gameButton.bind("<Button-3>", showMenu)

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
    runningLinux = platform in ["linux", "linux2"]
    for index, content in enumerate(menuData):
        if (not runningLinux and "windows" not in menuData[content]) or (runningLinux):
            menuRunFunction = getRunFunction(content, menuData[content])
            filemenu.add_command(label=content, command=menuRunFunction)

    filemenu.add_command(label="Quit", command=root.destroy)
    helpmenu.add_command(label="About", command=showAbout)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)
