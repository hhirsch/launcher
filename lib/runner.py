import os, subprocess
import json

class Runner:
    def __init__(self, executable, path, addShell):
        self.executable = executable.copy()
        self.path = path
        self.params = []
        self.addShell = addShell
        self.startup = []
    def addStartup(self, runner):
        self.startup.append(runner)
    def setStartup(self, runner):
        self.startup = []
        self.startup.append(runner)
    def setParams(self, params):
        self.params = params.copy()
    def addParam(self, param):
        self.params.append(param)
    def setExecutable(self, executable):
        self.executable = executable.copy()
    def addExecutable(self, executable):
        self.executable.append(executable)
    def setPath(self, path):
        self.path = path
    def run(self):
        path = self.path
        call = self.executable.copy()
        if self.params:
            for index, param in enumerate(self.params):
                call.append(param)
        if self.addShell:
            result = subprocess.run(call, cwd=path, capture_output=True, shell=True, check=True)
        else:
            result = subprocess.run(call, cwd=path, capture_output=False)
        return result
    def runStartup(self):
        if self.runners:
            for index, runner in enumerate(self.startup):
                runner.run()
    def getCall(self):
        call = self.executable.copy()
        if self.params:
            for index, param in enumerate(self.params):
                call.append(param)
        return call
    def toJson(self):
        data = self.toArray()
        if self.startup:
            data['startup'] = []
            for index, runner in enumerate(self.startup):
                data['startup'].append(runner.toArray())
        return json.dumps(data)

    def toArray(self):
        data = {}
        data['call'] = self.getCall()
        data['path'] = self.path
        if self.addShell:
            data['runInShell'] = "yes"
        else:
            data['runInShell'] = "no"
        return data
