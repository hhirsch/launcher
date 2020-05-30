import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image
import os, subprocess
from sys import platform

def print_hello():
    agePath = os.path.normpath('wololo-kingdoms/age2_x1')
    if platform in ["linux", "linux2"]:
        subprocess.call(["wine", "WK.exe"], cwd=agePath)
    else:
        subprocess.call("WK.exe", cwd=agePath)
    print('hello')

root = tk.Tk()
root.geometry("960x600")

annoImg = ImageTk.PhotoImage(Image.open("anno.jpg"))
aoeImg = ImageTk.PhotoImage(Image.open("aoe2.png"))

annoButton = tk.Button(root, text="anno", image=annoImg, command=print_hello)
annoButton.grid(row=1,column=1)

aoeButton = tk.Button(root, text="age", image=aoeImg, command=print_hello)
aoeButton.grid(row=1,column=2)

root.mainloop()
