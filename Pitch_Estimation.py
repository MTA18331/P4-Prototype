import scipy.io.wavfile as sp
import numpy as np
import matplotlib.pyplot as plt
import time
import random
import warnings

# Takes a numpy array as an input
def convert(array, duration):
    i = 0
    k = 0.6264  # The interval between  the base frequency
    complexNum = complex(0+0j)
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
            k += 0.645
            if k >= 7.076399999999998:
              k = 0.6264
            #print("i: ", i, "j: ", j)
            j += 1



        i += 1

    return frequency


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



def interval(freq, time):
    return freq*time


def plot(array, time):
    plt.plot(convert(array), interval(convert(array), time))
    plt.xlim(0, 20000)
    plt.ylim(-1000, 100000)
    plt.ylabel('Frequency')
    plt.xlabel('Interval')
    plt.show()




