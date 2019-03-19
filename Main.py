import Auto_Correlation
import Pitch_Estimation as pe
import Tempo_Detection
import LED
import warnings
import numpy as np
import matplotlib as plt
import scipy.io.wavfile as sp

with warnings.catch_warnings():
    warnings.simplefilter("ignore")  # Ignore annoying WavFileWarning
    sampleRate, samples = sp.read("Audio Files/3_tones.wav")  # Read Audio Files and the name of the intended audio file

#  SampleRate = number of samples per second and samples = 2D Array
print("SampleRate: ", sampleRate, " Number of samples: ", len(samples))
data = np.fft.fft(samples)  # Returns 2D array with complex numbers
time = data.shape[0]/sampleRate
print("Time: ", time)
freq = pe.convert(data, time)
print("Data: ", data[1])
print("Data: ", data[2])
print("Data: ", data[3])
print("freq: ", freq[1])
print("freq: ", freq[2])
print("freq: ", freq[3])
print("freq: ", freq[4])



pe.pitchCompare(freq)











