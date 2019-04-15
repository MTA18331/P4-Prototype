import scipy.io.wavfile as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.signal
import librosa
import time
import random
import warnings
import Enum_Classes as Enum
import pigpio as gp
import math


def load(enum):

    if enum == Enum.AudioFiles.tone1:  # Frequency = 30.86771, Note = B0
        tone_1, sampleRate = librosa.load('Audio Files/abc.wav', res_type='scipy')
        return tone_1, sampleRate
    elif enum == Enum.AudioFiles.tone2:  # Frequency = ???,
        tone_2, sampleRate = librosa.load('Audio Files/jacob_full1.wav', res_type='scipy')
        return tone_2, sampleRate


def plot(array,samplerate):
    #time = array.shape[0] / samplerate
    x_mag = np.absolute(array)
    f = np.linspace(0,samplerate,len(x_mag))
    #print(np.amax(array))
    #value = np.argmax(array)
    #print(array[value])
    #print(x_mag[value])

    #print(time)

    plt.figure(figsize=(13, 5))
    plt.plot(f, x_mag)
    plt.xlabel('Frequency Hz')
    plt.ylabel('Amplitude')

    plt.figure(figsize=(13, 5))
    plt.plot(f[270:570], x_mag[270:570])
    plt.xlabel('frequency HZ')
    plt.show()


def dft(array,minVal,maxVal):
    tmp = np.empty(shape=(maxVal-minVal), dtype=complex)
    if maxVal < len(array):
        interval = array[minVal:maxVal-1]
        tmp = np.fft.fft(interval)
    return tmp


def Estimate(array, sampleRate, deltaTime):

    numberOfSamples = int(sampleRate*deltaTime)  # Number of samples per time interval
    totalIterations = int(math.floor((len(array)/numberOfSamples)))  # Number of total iterations
    notes = np.empty(shape=(totalIterations, 1), dtype=Enum.Notes)    # Empty array which will be used to store notes in

    start = 0
    iterations = 50
    iterationNum = 0
    minValue = 1030   # Minimum value when looking for frequency
    maxValue = 1560   # Maximum value when looking for frequency
    tmpMin = minValue     # Temporary value used for calculating frequency
    # Empty array which will be used to store summations in correlating to each candidate frequency
    tmp = np.empty(shape=(maxValue - minValue, 1), dtype=complex)

    while iterationNum < totalIterations:
        minValue = tmpMin
        index = 0   # Index in temporary array

        while minValue < maxValue:
            scalar = 1  # Scalar used to multiply with the candidate frequency
            summation = 0   # Variable used to store the sum of each frequency
            while scalar <= iterations:
                if scalar*minValue+start < start+numberOfSamples:
                    summation += pow(np.abs(array[minValue*scalar+start]), 2)
                scalar += 1
            tmp[index] = summation
            index += 1
            minValue += 1

        freq = tmpMin + np.argmax(tmp)
        print("Start: ", start)
        print("Max Freq: ", np.argmax(tmp))
        print("Min Freq: ", np.argmin(tmp))
        print("Freq: ", freq)
        start += numberOfSamples

        if 1029 < freq <= 1105:     # Checking if the frequency matches the key being played
            notes[iterationNum] = Enum.Notes.C6
        elif 1358 < freq <= 1466:   # Checking if the frequency matches the key being played
            notes[iterationNum] = Enum.Notes.F6
        elif 1105 < freq <= 1244:   # Checking if the frequency matches the key being played
            notes[iterationNum] = Enum.Notes.D6
        elif 1244 < freq <= 1358:   # Checking if the frequency matches the key being played
            notes[iterationNum] = Enum.Notes.E6
        elif 1466 < freq <= 1628:   # Checking if the frequency matches the key being played
            notes[iterationNum] = Enum.Notes.G6
        # if the frequency is not within the ranges of the ones above, so we count it as there being no keys played
        else:
            notes[iterationNum] = Enum.Notes.N
        print("Note: ", notes)
        print("l: ", iterationNum)

        iterationNum += 1
    return notes


def harmonic(array, sampleRate, deltaTime):

    numberOfSamples = int(sampleRate*deltaTime)  # Number of samples per time interval

    iterations = 5
    minValue = 730   # Minimum value when looking for frequency
    maxValue = 1800   # Maximum value when looking for frequency
    tmpMin = minValue     # Temporary value used for calculating frequency
    # Empty array which will be used to store summations in correlating to each candidate frequency
    tmp = np.empty(shape=(len(array)), dtype=complex)
    index = 0 #index for tmp
    while minValue < maxValue:
        scalar = 1  # Scalar used to multiply with the candidate frequency
        summation = 0  # Variable used to store the sum of each frequency
        while scalar <= iterations:
            if scalar * minValue < numberOfSamples-1:
                summation += np.abs(array[minValue * scalar])**2
            scalar += 1
        tmp[index] = summation
        index += 1
        minValue += 1
    freq = tmpMin + np.argmax(tmp)
    if 730 < freq <= 900:
        return Enum.Notes.G5, freq
    elif 1029 < freq <= 1105:  # Checking if the frequency matches the key being played
        return Enum.Notes.C6, freq
    elif 1105 < freq <= 1244:  # Checking if the frequency matches the key being played
        return Enum.Notes.D6, freq
    elif 1244 < freq <= 1358:  # Checking if the frequency matches the key being played
        return Enum.Notes.E6, freq
    elif 1358 < freq <= 1466:  # Checking if the frequency matches the key being played
        return Enum.Notes.F6, freq
    elif 1466 < freq <= 1628:  # Checking if the frequency matches the key being played
        return Enum.Notes.G6, freq
    elif 1628 < freq <= 1800:  # Checking if the frequency matches the key being played
        return Enum.Notes.A6, freq
    # if the frequency is not within the ranges of the ones above, so we count it as there being no keys played
    else:
        return Enum.Notes.N, freq


def all():
    deltaTime = 1

    tone, sampleRate = load(Enum.AudioFiles.tone1)
    print(len(tone)/sampleRate)
    numberOfSamples = int(sampleRate * deltaTime)  # Number of samples per time interval
    maxIteration = int(math.floor((len(tone) / numberOfSamples)))  # Number of total iterations
    startIteration = 0
    minVal = 0
    maxVal = numberOfSamples
    notes = np.empty(shape=(maxIteration), dtype=Enum.Notes)
    while startIteration < maxIteration:
        fft = dft(tone,minVal,maxVal)
        note = harmonic(fft, sampleRate, deltaTime)
        notes[startIteration] = note
        #plot(fft, sampleRate)
        startIteration += 1
        minVal += numberOfSamples-1
        maxVal += numberOfSamples-1
    print(notes)


all()






