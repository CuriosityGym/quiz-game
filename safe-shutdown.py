#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess


GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.wait_for_edge(3, GPIO.FALLING)

try:
    while True:
         button_state = GPIO.input(3)
         if button_state == False:
             #GPIO.output(24, True)
             print('Shut down...')
             time.sleep(0.2)

except:
    GPIO.cleanup()
#subprocess.call(['shutdown', '-h', 'now'], shell=False)
