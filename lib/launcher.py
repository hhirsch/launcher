from os import path

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


def copyToProfile(game):
    print('hello')
