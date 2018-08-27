#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import pyttsx3;
import json
import requests
import time

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)
realAns = ""
players = [" player 1"," player 2"," player 3"," player 4"]
playerInputs = ["P1A","P1B","P1C","P1D","P2A","P2B","P2C","P2D","P3A","P3B","P3C","P3D","P4A","P4B","P4C","P4D"]
player1=0
player2=0
player3=0
player4=0
winner =""
points =10
reader = SimpleMFRC522.SimpleMFRC522()
noOfPlayers=0
playerEntry=""
startGame = False
playersConfirmed=False

f = open("quizGameRules.txt",'r')
gameRules = f.read()
engine.say(gameRules)
engine.runAndWait()
f.close()

'''
quizQuestions = {}  
quizQuestions['questionBank'] = []  
quizQuestions['questionBank'].append({  
    'question': 'Grand Central Terminal, Park Avenue, New York is the worlds',
    'a': 'largest railway station',
    'b': 'Longest railway station',
    'c': 'highest railway station',
    'd': 'busiest railway station',
    'answer':'largest railway station'
})
quizQuestions['questionBank'].append({  
    'question': 'Eritrea, which became the 182nd member of the UN in 1993, is in the continent of',
    'a': 'Asia',
    'b': 'Africa',
    'c': 'Europe',
    'd': 'Oceania',
    'answer':'Africa'
})
quizQuestions['questionBank'].append({  
    'question': 'What invention was alexander graham bell famous for ',
    'a': 'telephone',
    'b': 'television',
    'c': 'radiophone',
    'd': 'mobile phone',
    'answer':'telephone'
})

quizQuestions['questionBank'].append({  
    'question': 'For which of the following disciplines is the Nobel Prize awarded?',
    'a': 'Physics and Chemistry',
    'b': 'Physiology and Medicine',
    'c': 'Peace, Literature and Economics',
    'd': 'all of them',
    'answer':'all of them'
})
'''

#with open('quizQuestions.json', 'w') as outfile:  
#    json.dump(quizQuestions, outfile)



def answerInput():
    try:
        t0 = time.clock()
        while(time.clock()-t0 > 10):
            id, text = reader.read()
            print(id)
            print(text)
        #if (time.clock() -t0 > 15):
         #   text ='na'
    #except IndexError as e:
     #   print(e)
     #   engine.say("problem in reading your tag, please enter your answer again")
     #   engine.runAndWait()
    finally:
        GPIO.cleanup()
        
    return text


def updateScore(playerNum):
    if(playerNum == " player 1"):
        global player1
        player1 += points
    if(playerNum == " player 2"):
        global player2
        player2 += points
    if(playerNum == " player 3"):
        global player3
        player3 += points
    if(playerNum == " player 4"):
        global player4
        player4 += points

def winner(p1,p2,p3,p4):
    global winner
    if p1>p2 and p1 > p3 and p1>p4:
        winner = "player 1"
        return True
    if p2>p1 and p2 > p3 and p2>p4:
        winner = "player 2"
        return True
    if p3>p2 and p3 > p1 and p3>p4:
        winner = "player 3"
        return True
    if p4>p2 and p4 > p3 and p4>p1:
        winner = "player 4"
        return True
    if p1 == p2 and p1 == p3 and  p1==p4:
        print("its tie")
        return False
    elif p1 == p2 and p1 == p3:
        print("its tie")
        return False
    elif p1 == p2 and p1 == p4:
        print("its tie")
        return False
    elif p1 == p3 and p1 == p4:
        print("its tie")
        return False
    elif p2 == p3 and p2 == p4:
        print("its tie")
        return False
    elif p1 == p2:
        print("its tie")
        return False
    elif p1 == p3:
        print("its tie")
        return False
    elif p1 == p4:
        print("its tie")
        return False
    elif p2 == p3:
        print("its tie")
        return False
    elif p2 == p4:
        print("its tie")
        return False
    elif p3 == p4:
        print("its tie")
        return False

def shutdownRpi(halt):
   if halt == True:
     print("shutdown rpi")

#Ask for no of players
engine.say("How many players are there? ")
engine.runAndWait()
time.sleep(1)
engine.say("Player 1  please place your card")
engine.runAndWait()
while(playersConfirmed != True):
    t0=time.clock()
    print(round(t0))
    while(time.clock() - t0 < 15):
        playerEntry = answerInput()
        print(playerEntry[0:2])
        print(time.clock() - t0)
        if(playerEntry in playerInputs):
            noOfPlayers +=1
            engine.say('player ' + str(noOfPlayers) + 'added')
            engine.say('player ' + str(noOfPlayers + 1) + 'please place your card')
            engine.runAndWait()
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
    print(round(time.clock() - t0))
    if(round(time.clock() - t0) > 15):
        engine.say("No input from player")
        engine.runAndWait()
        if(noOfPlayers >=2):
           engine.say('are you sure you ewant continue with ' + str(noOfPlayers) + 'players')
           engine.say('player 1 please place your card to start the game')
           engine.runAndWait()
           confirm = answerInput()
           if(confirm[0:2] == 'P1'):
              playersConfirmed=True
              startGame = True 
        if(noOfPlayers <= 1):
            engine.say("You need minimum 2 players to start the game, go make some friends")
            startGame = False
            engine.runAndWait()

if(startGame == True):
    with open('quizQuestions.json') as json_file:
        data = json.load(json_file)
        i=0
        rounds = 1
        for q in data['questionBank']:
            engine.say('Round' + str(rounds))
            print("Round " + str(rounds))
            engine.say("Question for " + players[i])
            print('Question is: ' + q['question'])
            engine.say('Question is: ' + q['question'])
            print('option A: ' + q['a'])
            engine.say('option A: ' + q['a'])
            print('option B: ' + q['b'])
            engine.say('option B: ' + q['b'])
            print('option C: ' + q['c'])
            engine.say('option C: ' + q['c'])
            print('option D: ' + q['d'])
            engine.say('option D: ' + q['d'])
            engine.say(players[i] + 'Enter your answer ')
            engine.runAndWait()
            print("Enter your answer: ")
            #ans = raw_input("enter your answer :")
            ans = answerInput()
            print(ans[2])
            engine.say("You have selected option " + ans[2])
            engine.say("Are you sure, Do you want to lock option " + ans [2])
            engine.runAndWait()
            ans = answerInput()
            time.sleep(1)
            # id, text = reader.read()
            # ans = text
            print('answer is : ' + q['answer'])
            if(ans[2] == 'a' or ans[2] == 'A'):
               realAns = q['a']
            if(ans == 'b' or ans[2]== 'B'):
               realAns = q['b']
            if(ans == 'c' or ans[2]=='C'):
               realAns = q['c']
            if(ans == 'd' or ans[2]=='D'):
               realAns = q['d']   
            engine.say('answer is : ' + q['answer'])
            if(realAns == q['answer'] and str(i+1) == ans[1]):
               engine.say('Your answer is correct, 10 pointes to '+ players[i])
               updateScore(players[i])
            elif(realAns == q['answer'] and (str(i+1) != ans[1])):
               engine.say('Your answer is right but player ' + str(i+1) + 'did not give this answer. No points to player'+ str(i+1))
            else:
                engine.say('Your answer is wrong')
            print(player1)
            print(player2)
            print(player3)
            print(player4)
            i=i+1
            if(i>3):
                i=0
                engine.say('After ' + str(rounds) + 'rounds score is  ')
                rounds+=1
                engine.say('Player 1 '+ str(player1) + ' points.')
                engine.say('Player 2 '+ str(player2) + ' points.')
                engine.say('Player 3 '+ str(player3) + ' points.')
                engine.say('Player 4 '+ str(player4) + ' points.')
            engine.runAndWait()
            if rounds==4:
                engine.say('All rounds are over ')
                print("All rounds are over ")
                gameOver = winner(player1,player2,player3,player4)
                if(gameOver == True):    
                   engine.say("Winner is "+ winner)
                   print("Winner is" + winner)
                if(winner == False):
                   engine.say("Its a tie")
                   print("Its a tie")
                engine.say("Thank you for playing")
                engine.runAndWait()
                enagine.say("Do you want to play again? ")
                print("do you want to paly again?")
                playAgain = answerInput()
                if(playAgain == "yes" or playAgain == "Yes" or playAgain == "YES"):
                  newGame = True
                if(playAgain == "NO" or playAgain == "No" or playAgain == "no"):
                  newGame = Fasle
                  engine.say("Are you sure you want to end the game")
                  playAgain = answerInput()
                  if(playAgain == "yes" or playAgain == "Yes" or playAgain == "YES"): 
                     rpiHalt = True
                  if(playAgain == "no" or playAgain == "No" or playAgain == "NO"):
                    engine.say("Do you want to play Agian")
                    engine.runAndWait()

