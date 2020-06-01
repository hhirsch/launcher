from os import path
import os, subprocess
from .helper import getCachePath
from sys import platform

def runGenericGame(game, data):
    gamePath = os.path.normpath(getCachePath(game))
    linuxNative = False
    if "linux" in data and platform in ["linux", "linux2"]:
        gameData = data["linux"]
        linuxNative = True
    else:
        gameData = data["windows"]

    if "path" in gameData:
        gamePath = gamePath + '/' + gameData['path']

    call = [gameData['exe']]
    if not linuxNative:
        call.insert(0, "wine")

    if "params" in gameData:
        for index, param in enumerate(gameData['params']):
            call.append(param)

    subprocess.call(call, cwd=gamePath)
