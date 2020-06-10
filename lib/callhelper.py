import os, subprocess
from helper import getCachePath, copyToCache, gameIsInCache
from sys import platform
from shutil import which

def binaryFound(binary):
    return which(binary) is not None

def runGenericGameWithStartup(game, data):
    for index, param in enumerate(data['startup']):
        runGenericGame(game, data["startup"][param])

    runGenericGame(game, data)

def runGenericGame(game, data):
    if not gameIsInCache(game):
        copyToCache(game);
    path = os.path.normpath(getCachePath(game))
    runCommand(path, data)

def runCommand(path, data):
    path = os.path.normpath(path)
    linuxNative = False
    runningLinux = platform in ["linux", "linux2"]
    if "windows" in data:
        executable = data["windows"]

    if "linux" in data:
        if runningLinux and binaryFound(data["linux"]["exe"]):
            executable = data["linux"]
            linuxNative = True

    if "path" in executable:
        path = path + '/' + executable['path']

    call = [executable["exe"]]
    if not linuxNative and runningLinux:
        call.insert(0, "wine")

    if "params" in executable:
        for index, param in enumerate(executable['params']):
            call.append(param)
    subprocess.call(call, cwd=path)
