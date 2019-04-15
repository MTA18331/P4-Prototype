import tkinter
import Pitch_Estimation as pe

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk


def close_window():
    root.destroy()


root = tk.Tk()

root.text = tkinter.StringVar()
root.text.set("How many correct: ")

top = Frame(root)
middle = Frame(root)
middle2 = Frame(root)
bottom = Frame(root)

top.pack(side=TOP, fill=BOTH, expand=True)
middle.pack(side=TOP, fill=BOTH, expand=True)
middle2.pack(side=TOP, fill=BOTH, expand=True)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

startbutton = Button(root, text="Start", width=10, height=2, command=pe.all)
stopbutton = Button(root, text="Stop", width=10, height=2, command=pe.all)
Analyzebutton = Button(root, text="Analyse", width=10, height=2, command=pe.all)
howmanycorrectlabel = Label(root, textvariable=root.text)
exitbutton = Button(root, text="Exit", width=10, height=2, command=close_window)

startbutton.pack(in_=top, side=LEFT)
stopbutton.pack(in_=top, side=LEFT)
Analyzebutton.pack(in_=middle, side=LEFT)
howmanycorrectlabel.pack(in_=middle2, side=LEFT)
exitbutton.pack(in_=bottom, side=LEFT)

root.mainloop()