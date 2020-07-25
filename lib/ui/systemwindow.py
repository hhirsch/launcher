import tkinter as tk
from ui.color import Color
from ui.scrolledwindow import ScrolledWindow
from tkinter import scrolledtext, Frame, Label, ttk, CENTER, N, S, W, E, StringVar, OptionMenu

class SystemWindow:
    def __init__(self, root):
        self.messages = []
        self.root = root
        self.window = tk.Toplevel(root, bg=Color.darkBackground)
        self.text = scrolledtext.ScrolledText(self.window, undo=False, state='disabled')
        self.text.pack(expand=True, fill='both')
        self.window.title("System")
        self.window.geometry("460x470")
        self.window.resizable(0, 0)
        self.window.withdraw()
        self.window.protocol('WM_DELETE_WINDOW', self.hideWindow)
        self.currentRow = 0

    def addMessage(self, message):
        self.text.configure(state='normal')
        self.text.insert(tk.END, message)
        self.text.insert(tk.END, "\n")
        self.text.configure(state='disabled')

    def showWindow(self):
        self.window.deiconify()

    def hideWindow(self):
        self.window.withdraw()
