import tkinter as tk
from tkinter import ttk
from helper import getImagePath, gameIsInCache
from callhelper import runGenericGame, runGenericGameWithStartup
from assetexception import AssetException
from ui.color import Color

def removeBorders(widget):
    widget.config(borderwidth=0, highlightthickness=0)

def getImageOrException(game):
    import importlib
    pil = importlib.util.find_spec("PIL")
    found = pil is not None

    if(not found):
        raise AssetException("Image library not installed!")
    else:
        from PIL import ImageTk, Image
        image = Image.open(getImagePath(game)).convert('RGBA')
        if not gameIsInCache(game):
            downloadIconImage = Image.open(getImagePath("download"))
            image.paste(downloadIconImage)
        return ImageTk.PhotoImage(image)

def getRunFunction(game, data):
    if "startup" in data:
        runFunction = lambda: runGenericGameWithStartup(game, data)
    else:
        runFunction = lambda: runGenericGame(game, data)
    return runFunction

def createButton(root, game, data):
    runFunction = getRunFunction(game, data)
    try:
        gameImage = getImageOrException(game)
        gameButton = tk.Button(root, text=game, image=gameImage, command=runFunction)
        removeBorders(gameButton)
        Color.paintDark(gameButton)
        gameButton.image = gameImage
    except AssetException:
        gameButton = createButtonWithoutImage(root, game, data)
    return gameButton

def createButtonWithoutImage(root, game, data):
    runFunction = getRunFunction(game, data)
    invisiblePixel = tk.PhotoImage(width=1, height=1)
    gameButton = tk.Button(root, text=game, image=invisiblePixel, command=runFunction, height = 215-10, width = 460-10, compound="c", borderwidth=0)
    gameButton.image = invisiblePixel

    return gameButton
