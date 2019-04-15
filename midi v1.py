import pygame.midi
from pydub import AudioSegment
#from pydub.generators import Sine
from pydub.playback import play
import RPi.GPIO as GPIO
import time
#from gpiozero import Button
#import os

c = 35
d = 36
e = 33
f = 31
g = 32

# Setup of LEDs and setting them to low
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(f, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)

GPIO.output(c, GPIO.LOW)
GPIO.output(d, GPIO.LOW)
GPIO.output(e, GPIO.LOW)
GPIO.output(f, GPIO.LOW)
GPIO.output(g, GPIO.LOW)


switchPin = 11
GPIO.setup(switchPin, GPIO.IN)



def print_devices():
    for n in range(pygame.midi.get_count()):
        print (n,pygame.midi.get_device_info(n))


def playGame(input_device):
    LED = [35, 36, 33,35,35, 36, 33, 35, 33, 31, 32, 33, 31, 32] # = [c, d, e, c, c, d, e, c, e, f, g, e, f, g] #Sang: Mester Jakob
    LED_length = len(LED) #Variable which contains the LED Arrays length (used in the while loop)
    i = 0
    
    #print(LED[0] + " - on") #set LED[0] to high later
    GPIO.output(LED[0], GPIO.HIGH)
    
    while i < LED_length:
        
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
                
                if LED[i] == keyNote:
                    #print(LED[i] + " - off") #set LED[i] to low later
                    #play(soundC)
                    GPIO.output(LED[i], GPIO.LOW)
                    time.sleep(0.3)
                    i += 1
                    if i < LED_length:# so it doesn't give error
                        #print(LED[i] + " - on") #set LED[i] to high later
                        GPIO.output(LED[i], GPIO.HIGH)
                    else: # if you win
                        j=0
                        #Happy sound here
                        print("Win!")
                        while(j<20): #LEDs blinking
                            j+=1
                            GPIO.output(c, GPIO.LOW)
                            GPIO.output(d, GPIO.LOW)
                            GPIO.output(e, GPIO.LOW)
                            GPIO.output(f, GPIO.LOW)
                            GPIO.output(g, GPIO.LOW)
                            time.sleep(0.1)
                            
                            GPIO.output(c, GPIO.HIGH)
                            GPIO.output(d, GPIO.HIGH)
                            GPIO.output(e, GPIO.HIGH)
                            GPIO.output(f, GPIO.HIGH)
                            GPIO.output(g, GPIO.HIGH)
                            time.sleep(0.1)
                            
                        time.sleep(1)
                        break
                            
                
                else: # if you lose
                    #Sad sound here
                    print("Game over - All lights on!") #set all LEDs to high
                    GPIO.output(c, GPIO.HIGH)
                    GPIO.output(d, GPIO.HIGH)
                    GPIO.output(e, GPIO.HIGH)
                    GPIO.output(f, GPIO.HIGH)
                    GPIO.output(g, GPIO.HIGH)
        
                    time.sleep(3)
                    break
                
    playAgain(my_input)
                    
                
                
def number_to_note(number): #sets keyNumber to a keyNote
    notes = [35, 0, 36, 0, 33, 31, 0, 32, 0, 0, 0, 0] # = [c,c#,d,d#,e,f,f#,g,g#,a,a#,b] 
    
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
            
        print("Restarting the Game...")
        playGame(my_input)


if __name__ == '__main__':
    pygame.midi.init()
    print_devices()
    my_input = pygame.midi.Input(3) #midi keyboard id = 3
    playGame(my_input)
    #playAgain(my_input)
    
    

    