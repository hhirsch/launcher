from servicelocator import ServiceLocator
from ui.systemwindow import SystemWindow
from tkinter import Tk, Grid, Frame, N, S, E, W, Menu, messagebox, font

class ServiceLocatorFactory:
    @staticmethod
    def getServiceLocator(config):
        serviceLocator = ServiceLocator()
        serviceLocator.root = Tk()
        serviceLocator.systemWindow = SystemWindow(serviceLocator.root)
        return serviceLocator
