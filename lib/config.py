from os import path
import json

class Config:
    def __init__(self):
        self.data = {}

    def load(self, fileName):
        self.fileName = fileName
        if path.exists(fileName):
            with open(fileName) as fileHandle:
                self.data = json.load(fileHandle)
        else:
            raise AssetException("Config file not found!")

    def getValue(self, pathList):
        lastPathFragment = self.data
        for index, pathFragmentKey in enumerate(pathList):
            if pathFragmentKey in lastPathFragment:
                lastPathFragment = lastPathFragment[pathFragmentKey]
            else:
                raise IndexError("Key does not exist!")
        return lastPathFragment

    def hasValue(self, key):
        if key in self.getData():
            return True

        return False

    def getData(self):

        return self.data

    def getConfig(self, pathList):
        config = Config()
        config.data = self.getValue(pathList).copy()

        return config

    def setValue(self, key, value):
        self.data[key] = value
