import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()
audiofile = ""
root.text = tkinter.StringVar()


def pickfile():
    global audiofile
    audiofile = filedialog.askopenfilename(filetypes=((".WAV files", ".wav"),))
    labeltext = ("Current File:\n" + audiofile)
    root.text .set(labeltext)