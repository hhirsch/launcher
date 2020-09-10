import os, subprocess
from runner import Runner
from sys import platform
from helper import getCachePath
from config import Config

class RunnerFactory:
    @staticmethod
    def getConfigNeutralizeOperatingSystem(config):
        app = False
        newConfig = Config()
        nativeLinuxAvailable = False
        linuxPlatform = False
        executable = []
        if(config.hasValue("windows")):
            app = config.getConfig(["windows"])
            if app.hasValue("exe"):
                executable = [app.getValue(["exe"])]

        if platform in ["linux", "linux2"]:
            if executable:
                executable.insert(0, "wine")
            linuxPlatform = True
            if(config.hasValue("linux")):
                app = config.getConfig(["linux"])
                executable = [app.getValue(["exe"])]
                nativeLinuxAvailable = True

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
            pathValue = newConfig.getValue(["path"])
            path = getCachePath(pathValue)
        except:
            pass

        try:
            appName = newConfig.getValue(["appName"])
            path = getCachePath(appName)
        except Exception as e:
            pass

        try:
            appName = newConfig.getValue(["appName"])
            pathValue = newConfig.getValue(["path"])
            path = getCachePath(appName + '/' + pathValue)
        except:
            pass

        runner = Runner(executable, path, platform not in ["linux", "linux2"])
        try:
            params = newConfig.getValue(["params"])
            for param in params:
                runner.addParam(param)
        except:
            pass

        try:
            startupCommands = config.getValue(["startup"])
            for startupCommand in startupCommands:
                startupCommandConfig = config.getConfig(["startup", startupCommand])
                startupCommandConfig.setValue("appName", appName)
                startupRunner = RunnerFactory.getRunner(startupCommandConfig)
                runner.addStartup(startupRunner)
        except Exception as e:
            pass

        return runner
    @staticmethod
    def modifyRunner(runner, config):
        config = RunnerFactory.getConfigNeutralizeOperatingSystem(config)
        try:
            pathValue = config.getValue(["path"])
            path = getCachePath(pathValue)

        except:
            pass

        try:
            appName = config.getValue(["appName"])
            pathValue = config.getValue(["path"])
            path = getCachePath(appName + '/' + pathValue)
        except:
            pass
        runner.setPath(path)
        try:
            executable = config.getValue(['exe'])
            runner.setExecutable(executable)
        except:
            pass

        try:
            params = config.getValue(['params'])
            for param in params:
                runner.addParam(param)
        except:
            pass
        return runner
