#!/usr/bin/env python
 
import os
from time import sleep
 
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
 
 
os.system('flite -voice slt -t "Some rescue!" ')
 
sleep(0.1);
