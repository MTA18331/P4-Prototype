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
from tkinter import ttk

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
    root.bytes=0
    root.progress["value"] = root.bytes

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # Ignore annoying WavFileWarning
            sampleRate, samples = sp.read(audiofile)  # Read Audio Files and the name of the intended audio file
    #  SampleRate = number of samples per second and samples = 2D Array
        print("SampleRate: ", sampleRate, " Number of samples: ", len(samples))
        updateprogressbar()
        data = np.fft.fft(samples)  # Returns 2D array with complex numbers
        time = data.shape[0] / sampleRate
        print("Time: ", time)
        updateprogressbar()
        freq = pe.convert(data, time)
        print("Data: ", data[1])
        updateprogressbar()
        print("Data: ", data[2])
        updateprogressbar()
        print("Data: ", data[3])
        updateprogressbar()
        print("freq: ", freq[1])
        updateprogressbar()
        print("freq: ", freq[2])
        updateprogressbar()
        print("freq: ", freq[3])
        updateprogressbar()
        print("freq: ", freq[4])
        updateprogressbar()
        pe.pitchCompare(freq)
        updateprogressbar()
        pe.plot(pe.interval(freq,time),freq)


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
        SampleRatelabel = Label(root, textvariable=root.SampleRatelabeltext).pack(in_=middle, side=BOTTOM)
        NumberOfSampleslabel = Label(root, textvariable=root.NumberOfSampleslabeltext).pack(in_=middle, side=BOTTOM)
        timelabel = Label(root, textvariable=root.timelabeltext).pack(in_=middle, side=BOTTOM)
        date1label = Label(root, textvariable=root.date1labeltext).pack(in_=middle, side=BOTTOM)
        date2label = Label(root, textvariable=root.date2labeltext).pack(in_=middle, side=BOTTOM)
        date3label = Label(root, textvariable=root.date3labeltext).pack(in_=middle, side=BOTTOM)
        freq1label = Label(root, textvariable=root.freq1labellabeltext).pack(in_=middle, side=BOTTOM)
        freq2label = Label(root, textvariable=root.freq2labellabeltext).pack(in_=middle, side=BOTTOM)
        freq3label = Label(root, textvariable=root.freq3labellabeltext).pack(in_=middle, side=BOTTOM)
        freq4label = Label(root, textvariable=root.freq4labellabeltext).pack(in_=middle, side=BOTTOM)
        labelsVisible = True

def updateprogressbar():
    root.bytes += 10
    root.progress["value"] = root.bytes

def pickfile():
    global audiofile
    audiofile = filedialog.askopenfilename(filetypes=((".WAV files", ".wav"),))
    labeltext = ("Current File:\n" + audiofile)

    root.text .set(labeltext)



top = Frame(root)
middle = Frame(root)
middle2 = Frame(root)
bottom = Frame(root)

top.pack(side=TOP, fill=BOTH, expand=True)
middle.pack(side=TOP, fill=BOTH, expand=True)
middle2.pack(side=TOP, fill=BOTH, expand=True)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

root.progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
root.progress.pack(in_=bottom, side=LEFT)

root.maxbytes = 100
root.bytes = 0

root.progress["value"] = 0
root.progress["maximum"] = 100


openfileButton = Button(root, text="Open File", width=10, height=2, command=pickfile)
currentfilelabel = Label(root, text="current File", textvariable=root.text)
openfileButton.pack(in_=top, side=LEFT)
currentfilelabel.pack(in_=top, side=LEFT)

runaudioprocessingButton = Button(root, text="Run Audio Processing", width=20, height=2, command=audioProcessing, background='red')
runaudioprocessingButton.pack(in_=middle, side=LEFT)

turnOnLed = Button(root, text="Turn On LED", width=10, height=2, command=LED.turnOnLEDS)
turnOffLed = Button(root, text="Turn Of LED", width=10, height=2, command=LED.turnOffLEDS)
turnOnLed.pack(in_=middle2, side=LEFT)
turnOffLed.pack(in_=middle2, side=LEFT)





root.mainloop()






