from os import path
from assetexception import AssetException

def gameIsInProfile(game):
    return path.exists(helper.getProfilePath(game))

def gameIsInCache(game):
    return path.exists(helper.getCachePath(game))

def getCachePath(game):
    return path.normpath('repository/' + game)

def getProfilePath(game):
    return path.normpath('games/' + game)

def getImagePath(game):
    imagePath = path.normpath('data/images/' + game)
    if path.exists(imagePath + '.png'):
        return imagePath + '.png'

    if path.exists(imagePath + '.jpg'):
        return imagePath + '.jpg'

    raise AssetException("Image not found!")

def copyToProfile(game):
    print('hello')
