from enum import Enum


# Enum Class for octaves
class Octave(Enum):
    C4 = 1  # Frequency = 261.63, MIDI = 60
    C4S = 2  # Frequency = 277.18, MIDI = 61
    D4 = 3  # Frequency = 293.66, MIDI = 62
    D4S = 4  # Frequency = 311.13, MIDI = 63
    E4 = 5  # Frequency = 329.63, MIDI = 64
    F4 = 6  # Frequency = 349.23, MIDI = 65
    F4S = 7  # Frequency = 269.99, MIDI = 66
    G4 = 8  # Frequency = 392.00, MIDI = 67
    G4S = 9  # Frequency = 415.00, MIDI = 68
    A4 = 10  # Frequency = 440.00, MIDI = 69
    A4S = 11  # Frequency = 466.16, MIDI = 70
    B4 = 12  # Frequency = 493.88, MIDI = 71


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
