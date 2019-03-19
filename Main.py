import scipy.io.wavfile as sp
import numpy as np
import matplotlib.pyplot as plt
import warnings


# Takes a numpy array as an input
def convert(array, duration):
    i = 0
    k = 0.64
    frequency = np.empty(shape=(len(array), 1), dtype=np.complex)
    while i < 1:
        j = 1
        while j < len(array):
            if k != 0:
                scalar = duration*k
                frequency[j, i] = array[j, i]/scalar
                #print("Array: ", array[j])
            #print("i: ", i, "j: ", j)
            k += 0.64
            j += 1
        i += 1

    return frequency


def interval(freq, time):
    return freq*time


def plot(array, time):
    plt.plot(convert(array), interval(convert(array), time))
    plt.xlim(0, 20000)
    plt.ylim(-1000, 100000)
    plt.ylabel('Frequency')
    plt.xlabel('Interval')
    plt.show()


with warnings.catch_warnings():
    warnings.simplefilter("ignore")  # ignore annoying WavFileWarning
    sampleRate, samples = sp.read("Audio Files/Tone_2.wav")  # Write Audio Files and the name of the intended audio file


#  SampleRate = number of samples per second and samples = 2D Array
print("SampleRate: ", sampleRate, " Number of samples: ", len(samples))
data = np.fft.fft(samples)  # Returns 2D array with complex numbers
time = data.shape[0]/sampleRate
print("Time: ", time)
freq = convert(data, time)
print("freq: ", freq[2])










