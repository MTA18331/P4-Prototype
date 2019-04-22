import pygame.midi
import pygame
import RPi.GPIO as GPIO
import time
import Pitch_Estimation as pe
import numpy as np
import Enum_Classes as Enum
#from gpiozero import Button
#import os

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

cSound = pygame.mixer.Sound("Notes/c.wav")
dSound = pygame.mixer.Sound("Notes/D6.wav")
eSound = pygame.mixer.Sound("Notes/E6.wav")
fSound = pygame.mixer.Sound("Notes/F6.wav")
gSound = pygame.mixer.Sound("Notes/G6.wav")
aSound = pygame.mixer.Sound("Notes/A6.wav")
bSound = pygame.mixer.Sound("Notes/B6.wav")
c2Sound = pygame.mixer.Sound("Notes/C7.wav")
winSound = pygame.mixer.Sound("Notes/Fanfare.wav")
loseSound = pygame.mixer.Sound("Notes/Gameover.wav")

c = 35
d = 36
e = 33
f = 31
g = 32
a = 37
b = 38
c2 = 40

# Setup of LEDs and setting them to low
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(f, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c2, GPIO.OUT)

GPIO.output(c, GPIO.LOW)
GPIO.output(d, GPIO.LOW)
GPIO.output(e, GPIO.LOW)
GPIO.output(f, GPIO.LOW)
GPIO.output(g, GPIO.LOW)
GPIO.output(a, GPIO.LOW)
GPIO.output(b, GPIO.LOW)
GPIO.output(c2, GPIO.LOW)


#my_input = pygame.midi.Input(3)


def print_devices():
    for n in range(pygame.midi.get_count()):
        print (n,pygame.midi.get_device_info(n))

def Song(array):
    index = 0
    LED = np.empty(shape=(len(array)),dtype=int)
    while index <len(array):
        LED[index] = int(array[index])
        index+=1
    return LED


def playGame(LED, input_device):
     #Variable which contains the LED Arrays length (used in the while loop)
    i = 0
    #print(LED[0] + " - on") #set LED[0] to high later
    GPIO.output(int(LED[0]), GPIO.HIGH) 
        
    while i < len(LED):
        
        if input_device.poll(): #analysis of the Midi keyboards input
            event = input_device.read(1) #input is 3 arrays nested into each other event[data[midi[pressType, keyNumber,,]timeStamp]]
            data = event[0]
            midi = data[0]
            pressType = midi[0] #either 144 (on press) or 128 (on release)
            keyNumber = midi[1]
            keyNote = number_to_note(keyNumber)#gets the key note from the notes[]
            #print (pressType)
            if pressType == 144:
                print (keyNote)
                
                if int(LED[i]) == keyNote:
                    #print(LED[i] + " - off") #set LED[i] to low later
                    if keyNote == 35:
                        cSound.play()
                    elif keyNote == 36:
                        dSound.play()
                    elif keyNote == 33:
                        eSound.play()
                    elif keyNote == 31:
                        fSound.play()
                    elif keyNote == 32:
                        gSound.play()
                    elif keyNote == 37:
                        aSound.play()
                    elif keyNote == 38:
                        bSound.play()
                    elif keyNote == 40:
                        c2Sound.play()
                    
                    print (keyNote)
                    print(LED[i])
                    GPIO.output(int(LED[i]), GPIO.LOW)
                    time.sleep(0.3)
                    i += 1
                    if i < len(LED):# so it doesn't give error
                        #print(LED[i] + " - on") #set LED[i] to high later
                        GPIO.output(int(LED[i]), GPIO.HIGH)
                    else: # if you win
                        j=0
                        #Happy sound here
                        print("Win!")
                        winSound.play()
                        while(j<20): #LEDs blinking
                            j+=1
                            GPIO.output(c, GPIO.LOW)
                            GPIO.output(d, GPIO.LOW)
                            GPIO.output(e, GPIO.LOW)
                            GPIO.output(f, GPIO.LOW)
                            GPIO.output(g, GPIO.LOW)
                            GPIO.output(a, GPIO.LOW)
                            GPIO.output(b, GPIO.LOW)
                            GPIO.output(c2, GPIO.LOW)
                            time.sleep(0.1)
                            
                            GPIO.output(c, GPIO.HIGH)
                            GPIO.output(d, GPIO.HIGH)
                            GPIO.output(e, GPIO.HIGH)
                            GPIO.output(f, GPIO.HIGH)
                            GPIO.output(g, GPIO.HIGH)
                            GPIO.output(a, GPIO.HIGH)
                            GPIO.output(b, GPIO.HIGH)
                            GPIO.output(c2, GPIO.HIGH)
                            time.sleep(0.1)
                            
                        time.sleep(1)
                        break
                            
                
                else: # if you lose
                    #Sad sound here
                    print("Game over - All lights on!") #set all LEDs to high
                    loseSound.play()
                    GPIO.output(c, GPIO.HIGH)
                    GPIO.output(d, GPIO.HIGH)
                    GPIO.output(e, GPIO.HIGH)
                    GPIO.output(f, GPIO.HIGH)
                    GPIO.output(g, GPIO.HIGH)
                    GPIO.output(a, GPIO.HIGH)
                    GPIO.output(b, GPIO.HIGH)
                    GPIO.output(c2, GPIO.HIGH)
        
                    time.sleep(3)
                    break
                
    playAgain(my_input)
                
                
def number_to_note(number): #sets keyNumber to a keyNote
    notes = [35, 0, 36, 0, 33, 31, 0, 32, 0, 37, 0, 38] # = [c,c#,d,d#,e,f,f#,g,g#,a,a#,b] 
    
    return notes[number%12]

def playAgain(input_device):
    time.sleep(0.3)
    print("Play Again? Yes ofc!")
    time.sleep(0.3)
    
    if input_device.poll:
        #event = input_device.read(1)
        #print(event)
        #data = event[0]
        #midi = data[0]
        #pressType = midi[0]
        
        #if pressType == 144:
            
        GPIO.output(d, GPIO.LOW)
        GPIO.output(e, GPIO.LOW)
        GPIO.output(f, GPIO.LOW)
        GPIO.output(g, GPIO.LOW)
        GPIO.output(a, GPIO.LOW)
        GPIO.output(b, GPIO.LOW)
        GPIO.output(c2, GPIO.LOW)
            
        print("Restarting the Game...")
        #array = pe.loop()
        playGame(array,my_input)


if __name__ == '__main__':
    pygame.midi.init()
    print_devices()
    my_input = pygame.midi.Input(3) #midi keyboard id = 3
    array = pe.loop()
    LEDArray = Song(array)
    playGame(LEDArray, my_input)
    playAgain(my_input)
    
    

    
