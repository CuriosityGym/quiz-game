import pyttsx3;
import json
import requests
import time
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)
noOfPlayers=0
playerEntry=""
startGame = False
playersConfirmed=False
playerInputs = ["P1A","P1B","P1C","P1D","P2A","P2B","P2C","P2D","P3A","P3B","P3C","P3D","P4A","P4B","P4C","P4D"]
engine.say("How many players are there? ")
engine.runAndWait()
time.sleep(1)
engine.say("Player 1  please place your card")
engine.runAndWait()

while(playersConfirmed != True):
    t0=time.clock()
    print(round(t0))
    print(round(time.clock() - t0))
    
    while(time.clock() - t0 < 15):        
        playerEntry = input("enter your answer: ")
        print(playerEntry[0:2])
        if(playerEntry in playerInputs):
            noOfPlayers +=1
            engine.say('player ' + str(noOfPlayers) + 'added')
            engine.say('player ' + str(noOfPlayers + 1) + 'please place your card')
            engine.runAndWait()
            t0 = time.clock()
            if(playerEntry[0:2] == "P1"):
               playerInputs.remove('P1A')
               playerInputs.remove('P1B')
               playerInputs.remove('P1C')
               playerInputs.remove('P1D')
            if(playerEntry[0:2] == "P2"):
               playerInputs.remove('P2A')
               playerInputs.remove('P2B')
               playerInputs.remove('P2C')
               playerInputs.remove('P2D')
            if(playerEntry[0:2] == "P3"):
               playerInputs.remove('P3A')
               playerInputs.remove('P3B')
               playerInputs.remove('P3C')
               playerInputs.remove('P3D')
            if(playerEntry[0:2] == "P4"):
               playerInputs.remove('P4A')
               playerInputs.remove('P4B')
               playerInputs.remove('P4C')
               playerInputs.remove('P4D')
        print(playerInputs)
    if(round(time.clock() - t0) > 15):
        engine.say("No input from player")
        engine.runAndWait()
        if(noOfPlayers >=2):
           engine.say('are you sure you ewant continue with ' + str(noOfPlayers) + 'players')
           engine.say('player 1 please place your card to start the game')
           engine.runAndWait()
           confirm = input("enter your answer: ")
           if(confirm[0:2] == 'P1'):
              playersConfirmed=True
              startGame = True 
        if(noOfPlayers <= 1):
            engine.say("You need minimum 2 players to start the game, go make some friends")
            startGame = False
            engine.runAndWait()
