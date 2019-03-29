import scipy.io.wavfile as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.signal
import librosa
import time
import random
import warnings

# Takes a numpy array as an input

def pitchCompare(array):

    i = 0
    tmp = np.empty(shape=(len(array), 1), dtype=np.complex)
    min = complex(80+0j)
    max = complex(82+0j)

    min1 = complex(260 + 0j)
    max1 = complex(263 + 0j)

    min2 = complex(1900 + 0j)
    max2 = complex(2050 + 0j)
    max3 = complex(0 + 0j)

    while i < 1:
        j = 0
        while j < len(array):
            if min < array[j, i] < max:
                print('Freq: 80-82', j)
                tmp = array[j,i]
                print("Temp is: ", tmp)
            elif min1 < array[j, i] < max1:
                print('Freq: 260-263', j)
                tmp = array[j,i]
                print("Temp is: ", tmp)
            elif min2 < array[j, i] < max2:
                print('Freq: 1900-2050',j)
                tmp = array[j,i]
                print("Temp is: ", tmp)
            #elif  array[j, i] == max3:
             #   tmp = array[j,i]
                #   if random.randint(1,2) == 2:
                 #   print("No audio")
                  #  print(tmp)
            j += 1
        i += 1
    return tmp


def hammonicSum(array, lowLimit, highLimit,numOfInterval):

    tmp = np.empty(shape=(len(array), 1), dtype=np.complex)
    index = 0
    storedlimit = lowLimit
    complexNum = complex(0)
    scalar = 0
    while lowLimit < highLimit:

        while scalar < numOfInterval:
            if lowLimit*scalar < len(array):
                complexNum = pow(np.abs(array[lowLimit*scalar]), 2)+complexNum
            scalar += 1

        tmp[index] = complexNum
        index += 1
        scalar = 0
        lowLimit += 1
        complexNum = 0
        #print(np.argmax(tmp), "with value", np.amax(tmp))
    freq = storedlimit + np.argmax(tmp)
    print('this is frequency!!!!!',freq)
    return freq

def load(num):

    if num == 1:
        tone_1,sampleRate = librosa.load('Audio Files/Tone1.wav',res_type='scipy')
        return tone_1
    elif num == 2:
        tone_2,sampleRate = librosa.load('Audio Files/Tone2.wav',res_type='scipy')
        return tone_2
    elif num == 3:
        tone_3,sampleRate = librosa.load('Audio Files/Tone3.wav',res_type='scipy')
        return tone_3



def fft(array):
    data = np.fft.fft(array)
    #data2 = scipy.fft(x)

    return data

def plot(array,samplerate):
    time = array.shape[0] / samplerate
    x_mag = np.absolute(array)
    f = np.linspace(0,samplerate,len(x_mag))
    print(np.argmax(array))
    value = np.argmax(array)
    print(array[value])
    print(time)

    plt.figure(figsize=(13,5))
    plt.plot(f, x_mag)
    plt.xlabel('frequency hZ')

    plt.figure(figsize=(13,5))
    plt.plot(f[8000:11000],x_mag[8000:11000])
    plt.xlabel('frequency HZ')
    plt.show()

samplerate = 22050
lowLimit = 5200
highLimit = 5300
numOfInterval = 10
load(3)
fft(load(3))
hammonicSum(fft(load(3)),lowLimit,highLimit,numOfInterval)
plot(fft(load(3)), samplerate)



