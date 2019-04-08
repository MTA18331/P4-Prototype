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
    tone10 = "tone10"


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
    G5 = 78  # Frequency = 783.9909, MIDI = 78
    B6 = 83  # Frequency = 1975.533, MIDI = 83
    B5 = 82  # Frequency = 987.77, MIDI = 82
    C6 = 84  # Frequency = 1046.50, MIDI = 67
    D6 = 85  # Frequency = 1174.70, MIDI = 68
    E6 = 88  # Frequency = 1318.50, MIDI = 69
    F6 = 89  # Frequency = 1396.9, MIDI = 70
    G6 = 91  # Frequency = 1568.0, MIDI = 71
    A6 = 94  # Frequency = 1750.0, MIDI = 78

    N = 0

class Pins(Enum):
    D1 = 3 #
    D2 = 5
    D3 = 7
    D4 = 11
    D5 = 13
    D6 = 15
    D7 = 19
    D8 = 21



