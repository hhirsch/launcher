import os, subprocess
from runner import Runner
from sys import platform
from helper import getCachePath
from config import Config

class RunnerFactory:
    @staticmethod
    def getConfigNeutralizeOperatingSystem(config):
        newConfig = Config()
        nativeLinuxAvailable = False
        linuxPlatform = False
        executable = []
        try:
            app = config.getConfig(["windows"])
            executable = [app.getValue(["exe"])]
        except Exception as e:
            pass

        if platform in ["linux", "linux2"]:
            if executable:
                executable.insert(0, "wine")
            linuxPlatform = True
            try:
                app = config.getConfig(["linux"])
                executable = [app.getValue(["exe"])]
                nativeLinuxAvailable = True
            except:
                pass

        if not app:
            raise Exception("No executable found")

        try:
            path = app.getValue(["path"])
            newConfig.setValue("path", path)
        except:
            pass

        try:
            appName = config.getValue(["appName"])
            newConfig.setValue("appName", appName)
        except:
            pass

        newConfig.setValue("exe", executable)

        try:
            params = app.getValue(["params"])
            newConfig.setValue("params", params.copy())
        except:
            pass
        return newConfig
    @staticmethod
    def getRunner(config):
        path = None
        newConfig = RunnerFactory.getConfigNeutralizeOperatingSystem(config)
        executable = newConfig.getValue(["exe"])
        try:
            path = newConfig.getValue(["path"])
        except:
            pass
        try:
            appName = newConfig.getValue(["appName"])
            path = getCachePath(appName + '/' + path)
        except Exception as e:
            pass

        runner = Runner(executable, path)
        try:
            params = newConfig.getValue(["params"])
            for param in params:
                runner.addParam(param)
        except:
            pass
        return runner
    @staticmethod
    def modifyRunner(runner, config):
        config = RunnerFactory.getConfigNeutralizeOperatingSystem(config)
        try:
            executable = config.getValue(['exe'])
            runner.setExecutable(runner.executable + executable)
        except:
            pass

        try:
            params = config.getValue(['params'])
            for param in params:
                runner.addParam(param)
        except:
            pass
        print(runner.params)
        return runner
