#!/usr/bin/env python
 
import os
from time import sleep
 
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
msg = 'Hello all, Welcome to Who wants to be a millionaire. This is a quiz game. Rules of the games are rule 1 dont cheat and rule 2 dont answer for others question. Lets play. How many players are there player 1 place your card'
 
#os.system('flite -voice slt -t "Some rescue! my name is alexander, hello all who wants to be millionire. round 1 place yor card question for player 1 what is the capital of belgium" ')
os.system("flite -voice aup -t ' " + msg + " '" )


sleep(0.1);
