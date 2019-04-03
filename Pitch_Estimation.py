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


def hammonicSum(array, lowLimit, highLimit):

    tmp = np.empty(shape=(len(array), 1), dtype=np.complex)
    index = 0
    storedlimit = lowLimit
    complexNum = complex(0)
    scalar = 1
    numOfInterval = 10

    while lowLimit < highLimit:

        while scalar < numOfInterval:
            if lowLimit*scalar < len(array):
                complexNum = pow(np.abs(array[lowLimit*scalar]), 2) + complexNum
            scalar += 1

        tmp[index] = complexNum
        index += 1
        scalar = 1
        lowLimit += 1
        complexNum = 0

        #print(np.argmax(tmp), "with value", np.amax(tmp))

    freq = storedlimit + np.argmax(tmp)
    print(np.argmax(tmp))
    print('this is something', np.amax(tmp))
    print('this is something else!', freq)

    return freq


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
        tone_7, sampleRate = librosa.load('Audio Files/Tone2_82.wav', res_type='scipy')
        return tone_7, sampleRate
    elif enum == Enum.AudioFiles.tone8:  # Frequency = 1975.533, Note = B6
        tone_8, sampleRate = librosa.load('Audio Files/Tone_3_1975.wav', res_type='scipy')
        return tone_8, sampleRate
    elif enum == Enum.AudioFiles.tone9:  # Frequency = 783.9909, Note = G5
        tone_9, sampleRate = librosa.load('Audio Files/toneg5.wav', res_type='scipy')
        return tone_9, sampleRate


def fft(array):
    data = np.fft.fft(array)
    #data = scipy.fft(array)

    return data


def plot(array,samplerate):
    time = array.shape[0] / samplerate
    x_mag = np.absolute(array)
    f = np.linspace(0,samplerate,len(x_mag))
    print(np.argmax(array))
    #value = np.argmax(array)
    #print(array[value])
    #print(x_mag[value])

   #print(time)

    plt.figure(figsize=(13, 5))
    plt.plot(f, x_mag)
    plt.xlabel('Frequency Hz')
    plt.ylabel('Amplitude')

    plt.figure(figsize=(13, 5))
    plt.plot(f[1320:1370], x_mag[1320:1370])
    plt.xlabel('frequency HZ')
    plt.show()


lowLimit = 78
highLimit = 86
tone1, sampleRate = load(Enum.AudioFiles.tone4)
dft = fft(tone1)
hammonicSum(dft, lowLimit, highLimit)
plot(dft, sampleRate)



