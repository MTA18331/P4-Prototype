import scipy.io.wavfile as sp
import numpy as np
import matplotlib.pyplot as plt
import warnings


# Takes a numpy array as an input and converts to an array of base frequencies
def convert(array, duration):
    i = 0
    k = 0.64  # the interval between frequencies
    #  assign frequency to empty numpy array with complex numbers as data type which store the base frequency
    frequency = np.empty(shape=(len(array), 1), dtype=np.complex)
    while i < 1:  # x dimension (rows) in input array
        j = 1
        while j < len(array):  # y dimension (coloumns) in input array (Number of samples)
            if k != 0:  # if k does not equal 0 (since scalar must not be 0 which will crash the program)
                scalar = duration*k
                # Calculate base frequency by dividing frequency in fft array with scalar (interval)
                frequency[j, i] = array[j, i]/scalar  # assigns elements in frequency array to base frequency
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










