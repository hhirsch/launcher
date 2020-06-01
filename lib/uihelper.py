import tkinter as tk
from tkinter import PhotoImage, Label, messagebox
from PIL import ImageTk, Image
from helper import *
from assetexception import AssetException

def getRunFunction(game, data):
    runFunction = lambda: runGenericGame(game, data)
    return runFunction

def addGame(game, data, root):
    runFunction = getRunFunction(game, data)
    try:
        gameImage = ImageTk.PhotoImage(Image.open(getImagePath(game)))
        label = Label(image=gameImage)
        label.image = gameImage
        gameButton = tk.Button(root, text=game, image=gameImage, command=runFunction, borderwidth=0)
    except AssetException:
        invisiblePixel = tk.PhotoImage(width=1, height=1)
        label = Label(image=invisiblePixel)
        label.image = invisiblePixel
        gameButton = tk.Button(root, text=game, image=invisiblePixel, command=runFunction, height = 215-10, width = 460-10, compound="c", borderwidth=0)
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

def createWindowMenu(root, data):
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    helpmenu = tk.Menu(menubar, tearoff=0)
    menuData = data['launcher']['menu']
    for index, content in enumerate(menuData):
        menuRunFunction = getRunFunction(content, menuData[content])
        filemenu.add_command(label=content, command=menuRunFunction)

    filemenu.add_command(label="Quit", command=root.destroy)
    helpmenu.add_command(label="About", command=showAbout)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)
