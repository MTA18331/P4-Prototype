import scipy.io.wavfile as sp
import numpy as np
import matplotlib.pyplot as plt


# Takes a numpy array as an input
def convert(array):
    i = 0
    k = 0.64
    while i < 1:
        j = 1
        while j < len(array):
            if k != 0:
                scalar = time*k
                freq = array[j]/scalar

        k += 0.64
        j += 1
    i += 1


def interval(freq, time):
    return freq*time


def plot(array, time):
    plt.plot(convert(array), interval(convert(array), time))
    plt.xlim(0, 20000)
    plt.ylim(-1000, 100000)
    plt.ylabel('Frequency')
    plt.xlabel('Interval')
    plt.show()


# Write Audio Files/ and then the name of the intended audio file
sampleRate, samples = sp.read("Audio Files/Tone_2.wav")
#  SampleRate = number of samples per second and samples = 2D Array
print("SampleRate: ", sampleRate, " sample: ", samples)
data = np.fft.fft(samples) # Returns 2D array with complex numbers
time = data.shape[0]/sampleRate
print("Time: ", time)







