import tkinter
import Auto_Correlation
import Pitch_Estimation as pe
import Tempo_Detection
import LED
import warnings
import numpy as np
import matplotlib as plt
import scipy.io.wavfile as sp
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


root = tk.Tk()
audiofile = ""
root.text = tkinter.StringVar()


def audioProcessing():
    global audiofile
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # Ignore annoying WavFileWarning
            sampleRate, samples = sp.read(audiofile)  # Read Audio Files and the name of the intended audio file
    #  SampleRate = number of samples per second and samples = 2D Array
        print("SampleRate: ", sampleRate, " Number of samples: ", len(samples))
        data = np.fft.fft(samples)  # Returns 2D array with complex numbers
        time = data.shape[0] / sampleRate
        print("Time: ", time)
        freq = pe.convert(data, time)
        print("Data: ", data[1])
        print("Data: ", data[2])
        print("Data: ", data[3])
        print("freq: ", freq[1])
        print("freq: ", freq[2])
        print("freq: ", freq[3])
        print("freq: ", freq[4])
        pe.pitchCompare(freq)

        SampleRatelabel = Label(root, text="SampleRate: " + '%s' % sampleRate, ).pack(anchor=S)
        NumberOfSampleslabel = Label(root, text="Number of samples: " + '%s' % len(samples), ).pack(anchor=S)
        timelabel = Label(root, text="Time: " + '%s' % time, ).pack(anchor=S)
        date1label = Label(root, text="Data: " + '%s' % data[1], ).pack(anchor=S)
        date2label = Label(root, text="Data: " + '%s' % data[2], ).pack(anchor=S)
        date3label = Label(root, text="Data: " + '%s' % data[3], ).pack(anchor=S)
        freq1label = Label(root, text="Freq: " + '%s' % freq[1], ).pack(anchor=S)
        freq2label = Label(root, text="Freq: " + '%s' % freq[2], ).pack(anchor=S)
        freq3label = Label(root, text="Freq: " + '%s' % freq[3], ).pack(anchor=S)
        freq4label = Label(root, text="Freq: " + '%s' % freq[4], ).pack(anchor=S)
    except FileNotFoundError:
        messagebox.showinfo("Nope", "Choose a file first!")


def pickfile():
    global audiofile
    audiofile = filedialog.askopenfilename(filetypes=((".WAV files", ".wav"),))
    labeltext = ("Current File:\n" + audiofile)

    root.text .set(labeltext)


b1 = Button(root, text='Open File', command=pickfile).pack(anchor=N)
currentfilelabel = Label(root, text="current File", textvariable=root.text).pack(anchor=CENTER)
b2 = Button(root, text='Run Audio Processing', command=audioProcessing, background='red').pack(anchor=S)
root.mainloop()






