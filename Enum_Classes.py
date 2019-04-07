from enum import Enum


# Enum Class for Audio Files
class AudioFiles(Enum):
    tone1 = "tone1"
    tone2 = "tone2"
    tone3 = "tone3"
    tone4 = "tone4"
    tone5 = "tone5"
    tone6 = "tone6"
    tone7 = "tone7"
    tone8 = "tone8"
    tone9 = "tone9"


# Octave number
class Octaves(Enum):
    oct1 = 1
    oct2 = 2
    oct3 = 3
    oct4 = 4
    oct5 = 5
    oct6 = 6
    oct7 = 7
    oct8 = 8


# Enum Class for octaves
class Notes(Enum):
    E2 = 40  # Frequency = 82.407, MIDI = 40
    C4 = 60  # Frequency = 261.63, MIDI = 60
    C4S = 61  # Frequency = 277.18, MIDI = 61
    D4 = 62  # Frequency = 293.66, MIDI = 62
    D4S = 63  # Frequency = 311.13, MIDI = 63
    E4 = 64  # Frequency = 329.63, MIDI = 64
    F4 = 65  # Frequency = 349.23, MIDI = 65
    F4S = 66  # Frequency = 269.99, MIDI = 66
    G4 = 67  # Frequency = 392.00, MIDI = 67
    G4S = 68  # Frequency = 415.00, MIDI = 68
    A4 = 69  # Frequency = 440.00, MIDI = 69
    A4S = 70  # Frequency = 466.16, MIDI = 70
    B4 = 71  # Frequency = 493.88, MIDI = 71
    B6 = 83  # Frequency = 1975.533, MIDI = 83
    N = None



