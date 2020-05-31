from __future__ import print_function
from subprocess import call
from shutil import which
from datetime  import datetime

def log(message):
    print(datetime.now().strftime("%a %b %d %H:%M:%S") + " - " + str(message))

def isToolAvailable(name):
    """Check whether tool exists and is executable."""

    return which(name) is not None

def installPip():
    """
    Pip is the standard package manager for Python. Starting with Python 3.4
    it's included in the default installation, but older versions may need to
    download and install it. This code should pretty cleanly do just that.
    """
    log("Installing pip, the standard Python Package Manager")
    from os     import remove
    from urllib import urlretrieve
    urlretrieve("https://bootstrap.pypa.io/get-pip.py", "get-pip.py")
    call(["python", "get-pip.py"])
    remove("get-pip.py")

def getPip():
    """
    Pip is the standard package manager for Python.
    This returns the path to the pip executable, installing it if necessary.
    """
    from os.path import isfile, join

    if not isToolAvailable("pip"):
        installPip(log)
        if not isToolAvailable("pip"):
            raise("Failed to find or install pip!")
    return "pip"

def installIfNeeded(moduleName, nameOnPip=None, notes=""):
    """ Installs a Python library using pip, if it isn't installed. """
    from pkgutil import iter_modules

    # Check if the module is installed
    if moduleName not in [tuple_[1] for tuple_ in iter_modules()]:
        log("Installing " + moduleName + notes + " Library for Python")
        call([getPip(), "install", nameOnPip if nameOnPip else moduleName])

installIfNeeded("Pillow")
call(["python", "launcher-ui.py"])
