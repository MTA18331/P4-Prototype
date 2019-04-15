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
#import RPi.GPIO as GPIO
# Takes a numpy array as an input


def load(enum):

    if enum == Enum.AudioFiles.tone1:  # Frequency = 30.86771, Note = B0
        tone_1, sampleRate = librosa.load('Audio Files/Tone1.wav', res_type='scipy')
        return tone_1, sampleRate
    elif enum == Enum.AudioFiles.tone2:  # Frequency = 783.9909, Note = G5
        tone_2, sampleRate = librosa.load('Audio Files/Tone2.wav', res_type='scipy')
        return tone_2, sampleRate
    elif enum == Enum.AudioFiles.tone3:  # Frequency = 5274.04, Note = B8
        tone_3, sampleRate = librosa.load('Audio Files/Tone3.wav', res_type='scipy')
        return tone_3, sampleRate
    elif enum == Enum.AudioFiles.tone4:  # tone_6, tone_7, tone_8
        tone_4, sampleRate = librosa.load('Audio Files/3_tones.wav', res_type='scipy')
        return tone_4, sampleRate
    elif enum == Enum.AudioFiles.tone5:  # Frequency = 783.9909, Note = G5
        tone_5, sampleRate = librosa.load('Audio Files/G5piano.wav', res_type='scipy')
        return tone_5, sampleRate
    elif enum == Enum.AudioFiles.tone6:  # Frequency = 261.63, Note = C4
        tone_6, sampleRate = librosa.load('Audio Files/Tone_1_261.wav', res_type='scipy')
        return tone_6, sampleRate
    elif enum == Enum.AudioFiles.tone7:  # Frequency = 82.41, Note = E2
        tone_7, sampleRate = librosa.load('Audio Files/Tone_2_82.wav', res_type='scipy')
        return tone_7, sampleRate
    elif enum == Enum.AudioFiles.tone8:  # Frequency = 1975.533, Note = B6
        tone_8, sampleRate = librosa.load('Audio Files/Tone_3_1975.wav', res_type='scipy')
        return tone_8, sampleRate
    elif enum == Enum.AudioFiles.tone9:  # Frequency = 783.9909, Note = G5
        tone_9, sampleRate = librosa.load('Audio Files/toneg5.wav', res_type='scipy')
        return tone_9, sampleRate
    elif enum == Enum.AudioFiles.tone10:  # Frequency = ???,
        tone_10, sampleRate = librosa.load('Audio Files/jacob1.wav', res_type='scipy')
        return tone_10, sampleRate
    elif enum == Enum.AudioFiles.tone11:  # Frequency = ???,
        tone_11, sampleRate = librosa.load('Audio Files/jacob2.wav', res_type='scipy')
        return tone_11, sampleRate
    elif enum == Enum.AudioFiles.tone12:  # Frequency = ???,
        tone_12, sampleRate = librosa.load('Audio Files/jacob_32.wav', res_type='scipy')
        return tone_12, sampleRate
    elif enum == Enum.AudioFiles.tone13:  # Frequency = ???,
        tone_13, sampleRate = librosa.load('Audio Files/jacob_160.wav', res_type='scipy')
        return tone_13, sampleRate


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
    tmp = np.empty(shape=(maxVal-minVal, 1), dtype=complex)
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
   # print('NUM', numberOfSamples)
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
    totalIterations = int(math.floor((len(array) / numberOfSamples)))  # Number of total iterations
    notes = np.empty(shape=(totalIterations, 1), dtype=Enum.Notes)

    iterations = 5
    minValue = 1040   # Minimum value when looking for frequency
    maxValue = 1580   # Maximum value when looking for frequency
    tmpMin = minValue     # Temporary value used for calculating frequency
    # Empty array which will be used to store summations in correlating to each candidate frequency
    tmp = np.empty(shape=(len(array), 1), dtype=complex)
    index = 0
    while minValue < maxValue:
        scalar = 1  # Scalar used to multiply with the candidate frequency
        summation = 0  # Variable used to store the sum of each frequency
        while scalar < iterations:
            if scalar * minValue < numberOfSamples-1:
                summation += pow(np.abs(array[minValue * scalar]), 2)
            scalar += 1
        tmp[index] = summation
        index += 1
        minValue += 1
        freq = tmpMin + np.argmax(tmp)

    if 1029 < freq <= 1105:  # Checking if the frequency matches the key being played
        return Enum.Notes.C6, freq
    elif 1358 < freq <= 1466:  # Checking if the frequency matches the key being played
        return Enum.Notes.F6, freq
    elif 1105 < freq <= 1244:  # Checking if the frequency matches the key being played
        return Enum.Notes.D6, freq
    elif 1244 < freq <= 1358:  # Checking if the frequency matches the key being played
        return Enum.Notes.E6, freq
    elif 1466 < freq <= 1628:  # Checking if the frequency matches the key being played
        return Enum.Notes.G6, freq
    # if the frequency is not within the ranges of the ones above, so we count it as there being no keys played
    else:
        return Enum.Notes.N, freq


def all():
    deltaTime = 1

    tone, sampleRate = load(Enum.AudioFiles.tone12)
    print(len(tone)/sampleRate)
    numberOfSamples = int(sampleRate * deltaTime)  # Number of samples per time interval
    maxIteration = int(math.floor((len(tone) / numberOfSamples)))  # Number of total iterations
    startIteration = 0
    minVal = 0
    maxVal = numberOfSamples

    while startIteration < maxIteration:
        fft = dft(tone,minVal,maxVal)
        tmp = harmonic(fft, sampleRate, deltaTime)
        #plot(fft, sampleRate)
        print(tmp)
        startIteration += 1
        minVal += numberOfSamples-1
        maxVal += numberOfSamples-1






all()
'''
tone, sampleRate = load(Enum.AudioFiles.tone10)
dft = dft(tone)
#plot(dft, sampleRate)
deltaTime = 0.33
tmp = Estimate(tone, sampleRate, deltaTime)
plot(tone, sampleRate)
'''







