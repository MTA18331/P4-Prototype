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
labelsVisible = False
#<editor-fold desc="tkinter string variables">
root.text = tkinter.StringVar()
root.SampleRatelabeltext = tkinter.StringVar()
root.NumberOfSampleslabeltext = tkinter.StringVar()
root.timelabeltext = tkinter.StringVar()
root.date1labeltext = tkinter.StringVar()
root.date2labeltext = tkinter.StringVar()
root.date3labeltext = tkinter.StringVar()
root.freq1labellabeltext = tkinter.StringVar()
root.freq2labellabeltext = tkinter.StringVar()
root.freq3labellabeltext = tkinter.StringVar()
root.freq4labellabeltext = tkinter.StringVar()
#</editor-fold>


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


        buildlabels(sampleRate,samples, time,data,freq)

    except FileNotFoundError:
        messagebox.showinfo("Nope", "Choose a file first!")


def buildlabels(sampleRate, samples, time, data, freq):
    global labelsVisible
    root.SampleRatelabeltext.set("SampleRate: " + '%s' % sampleRate, )
    root.NumberOfSampleslabeltext.set("Number of samples: " + '%s' % len(samples), )
    root.timelabeltext.set("Time: " + '%s' % time)
    root.date1labeltext.set("Data: " + '%s' % data[1])
    root.date2labeltext.set("Data: " + '%s' % data[2])
    root.date3labeltext.set("Data: " + '%s' % data[3])
    root.freq1labellabeltext.set("Freq: " + '%s' % freq[1])
    root.freq2labellabeltext.set("Freq: " + '%s' % freq[2])
    root.freq3labellabeltext.set("Freq: " + '%s' % freq[3])
    root.freq4labellabeltext.set("Freq: " + '%s' % freq[4])
    if not labelsVisible:
        SampleRatelabel = Label(root, textvariable=root.SampleRatelabeltext).pack(anchor=S)
        NumberOfSampleslabel = Label(root, textvariable=root.NumberOfSampleslabeltext).pack(anchor=S)
        timelabel = Label(root, textvariable=root.timelabeltext).pack(anchor=S)
        date1label = Label(root, textvariable=root.date1labeltext).pack(anchor=S)
        date2label = Label(root, textvariable=root.date2labeltext).pack(anchor=S)
        date3label = Label(root, textvariable=root.date3labeltext).pack(anchor=S)
        freq1label = Label(root, textvariable=root.freq1labellabeltext).pack(anchor=S)
        freq2label = Label(root, textvariable=root.freq2labellabeltext).pack(anchor=S)
        freq3label = Label(root, textvariable=root.freq3labellabeltext).pack(anchor=S)
        freq4label = Label(root, textvariable=root.freq4labellabeltext).pack(anchor=S)
        labelsVisible = True


def pickfile():
    global audiofile
    audiofile = filedialog.askopenfilename(filetypes=((".WAV files", ".wav"),))
    labeltext = ("Current File:\n" + audiofile)

    root.text .set(labeltext)


b1 = Button(root, text='Open File', command=pickfile).pack(anchor=N)
currentfilelabel = Label(root, text="current File", textvariable=root.text).pack(anchor=CENTER)
b2 = Button(root, text='Run Audio Processing', command=audioProcessing, background='red').pack(anchor=S)
root.mainloop()






