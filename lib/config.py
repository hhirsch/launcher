from os import path
import json

class Config:
    def __init__(self, fileName):
        self.fileName = fileName
        if path.exists(fileName):
            with open(fileName) as fileHandle:
                self.data = json.load(fileHandle)
        else:
            raise AssetException("Config file not found!")

    # input ["path", "to", "config", "setting"]
    def getValue(self, pathList):
        if pathList[0] in self.data:
            lastPathFragment = self.data[pathList[0]]
        else:
            raise IndexError("Key does not exist!")
        lastPathFragment = self.data;
        for index, pathFragmentKey in enumerate(pathList):
            if pathFragmentKey in lastPathFragment:
                lastPathFragment = lastPathFragment[pathFragmentKey]

        return lastPathFragment
