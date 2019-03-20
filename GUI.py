
from tkinter import *
import tkinter as tk
import Main
from tkinter import messagebox
from tkinter import filedialog
# create the main sections of the layout,
# and lay them out

"""""""""
def pickfile():

    audiofile = filedialog.askopenfilename(filetypes=((".WAV files", ".wav"),))
    #Main.labeltext = ("Current File:\n" + Main.audiofile)
    print (audiofile)
    #Main.root.text .set(Main.labeltext)


root = tk.Tk()
top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

# create the widgets for the top part of the GUI,
# and lay them out
openfileButton = Button(root, text="Open File", width=10, height=2, command=pickfile())
runaudioprocessingButton = Button(root, text="Run Audio Processing", width=10, height=2, command=Main.audioProcessing(), background='red')
openfileButton.pack(in_=top, side=LEFT)
runaudioprocessingButton.pack(in_=top, side=LEFT)

# create the widgets for the bottom part of the GUI,
# and lay them out
text = Text(root, width=35, height=15)
scrollbar = Scrollbar(root)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
scrollbar.pack(in_=bottom, side=RIGHT, fill=Y)
text.pack(in_=bottom, side=LEFT, fill=BOTH, expand=True)

root.mainloop() """