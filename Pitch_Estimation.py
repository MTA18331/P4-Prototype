import scipy.io.wavfile as sp
import numpy as np
import matplotlib.pyplot as plt
import warnings

# Takes a numpy array as an input
def convert(array, duration):
    i = 0
    k = 0.64  # The interval between  the base frequency
    # Assigns frequency to empty array with the data type complex numbers
    frequency = np.empty(shape=(len(array), 1), dtype=np.complex)
    while i < 1:  # x dimension in input array
        j = 1
        while j < len(array):  # y dimension in input array
            if k != 0:
                # k must not be zero because that will cause scalar to divide by zero which will crash the program
                scalar = duration*k
                #  Base frequency equals element in fft array divide by the scalar which is time duration times interval between frequencies
                frequency[j, i] = array[j, i]/scalar  # assigns an element in the frequency array to be equal to the base frequency.
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


