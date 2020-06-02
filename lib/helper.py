from os import path
from assetexception import AssetException
from shutil import copytree

def gameIsInRepository(game):
    return path.exists(getRepositoryPath(game))

def gameIsInCache(game):
    return path.exists(getCachePath(game))

def getCachePath(game):
    return path.normpath('games/' + game)

def getRepositoryPath(game):
    return path.normpath('repository/' + game)

def getImagePath(game):
    imagePath = path.normpath('data/images/' + game)
    if path.exists(imagePath + '.png'):
        return imagePath + '.png'

    if path.exists(imagePath + '.jpg'):
        return imagePath + '.jpg'

    raise AssetException("Image not found!")

def copyToCache(game):
    if not path.exists(getCachePath(game)):
        if path.isdir(getRepositoryPath(game)):
            copytree(getRepositoryPath(game), getCachePath(game))

