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
tags = ["P1A","P1B","P1C","P1D","P2A","P2B","P2C","P2D","P3A","P3B","P3C","P3D","P4A","P4B","P4C","P4D","GR","EG"]
players = [" player 1"," player 2"," player 3"," player 4"]
playerInputs = ["P1A","P1B","P1C","P1D","P2A","P2B","P2C","P2D","P3A","P3B","P3C","P3D","P4A","P4B","P4C","P4D"]
player1=0
player2=0
player3=0
player4=0
playerScores=[0,0,0,0]
winner =""
points =10
reader = SimpleMFRC522.SimpleMFRC522()
noOfPlayers=0
playerEntry=""
startGame = False
playersConfirmed=False
validInput = False
error=False
endGame = False

def readRules():
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
    text = ""
    try:
        #t0 = time.clock()
       # global playerEntry
        while text not in tags:
            engine.say("Place your card: ")
            engine.runAndWait()
            id, text = reader.read()
            print(id)
            print(text)
            text1 = text
            print(text1)
            if(text1 == "P1C"):
               print("matched")
        
    
    finally:
        GPIO.cleanup()
        
    return text

#updateScore(players[i],points,noOfPlayers)
def updateScore(playerNum, increment, numberOfPlayers):
    global playerScores
    for i in range(0,numberOfPlayers):
        if(playerNum==players[i]):
            playerScores[i]= playerScores[i]+10
'''
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
'''
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


readRules()

#Ask for no of players
engine.say("How many players are there? ")
engine.say("Player 1  please place your card")
engine.runAndWait()
time.sleep(1)
while(playersConfirmed != True):
    #t0=time.clock()
    #print(round(t0))
    #while(time.clock() - t0 < 15):
    playerEntry = answerInput()
    prevEntry = playerEntry
    print(playerEntry[0:2])
    #print(time.clock() - t0)
    if(playerEntry[0:3] in playerInputs):
        noOfPlayers +=1
        engine.say('player ' + str(noOfPlayers) + 'added')
        engine.runAndWait() 
        if(noOfPlayers == 1):
           engine.say('player ' + str(noOfPlayers + 1) + 'please place your card')
           engine.runAndWait()
        t0=time.clock()
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
    #print(round(time.clock() - t0))
        if(noOfPlayers >= 2):
            if(noOfPlayers == 2): 
               engine.say("Do you want to play with 2 players then player 1 place your card if want to add more players then player 2 place your card")
               engine.runAndWait()
               playerEntry = answerInput()
               if(playerEntry[0:2] == prevEntry[0:2]):
                   engine.say('player ' + str(noOfPlayers + 1) + 'please place your card')
                   engine.runAndWait()
               if(playerEntry[0:2] == "P1"):
                   playersConfirmed=True
                   startGame =True
            if(noOfPlayers ==3):
               engine.say("Do you want to play with 3 players then player 1 place your card if want to add more players then player 3 place your card")
               engine.runAndWait()
               playerEntry = answerInput()
               if(playerEntry[0:2] == prevEntry[0:2]):
                   engine.say('player ' + str(noOfPlayers + 1) + 'please place your card')
                   engine.runAndWait()
               if(playerEntry[0:2] == "P1"):
                   playersConfirmed=True
                   startGame =True
            if(noOfPlayers ==4):
               engine.say("Do you want to play with 3 players then player 1 place your card if want to add more players then player 3 place your card")
               engine.runAndWait()
               playerEntry = answerInput()
               if(playerEntry[0:2] == prevEntry[0:2]):
                   engine.say('player ' + str(noOfPlayers + 1) + 'please place your card')
                   engine.runAndWait()
               if(playerEntry[0:2] == "P1"):
                   playersConfirmed=True
                   startGame =True
            '''if(noOfPlayers <= 1):
                engine.say("You need minimum 2 players to start the game, go make some friends")
                startGame = False
                engine.runAndWait()'''

if(startGame == True):
    engine.say("Welcome all " + str(noOfPlayers) + " players, All the best, Lets play ")
    engine.runAndWait()
    with open('quizQuestions.json') as json_file:
        data = json.load(json_file)
        i=0
        rounds = 0
        for q in data['questionBank']:
            engine.say('Round' + str(rounds+1))
            print("Round " + str(rounds+1))
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
            
            if(ans[0:2] == "EG"):
                print("Confirm??")
                enagine.say("Are you sure you want to end game, to end game place end game card again,  if you place that card by mistake then place card of any player to continue the game")
                engine.runAndWait()
                end = answerInput()
                if(end[0:2] == "EG"):
                   areYousure = True
            elif(ans[0:2] == "GR"):
                readRules()
                enagine.say("Now enter you answer")
                engine.runAndWait()
                ans = answerInput()
            else:    
                try:
                     if(ans[0:2] == "P1" or ans[0:2] == "P2" or ans[0:2] == "P3" or ans[0:2] == "P4"):
                        print(ans[2])
                        print('run try block')
                        validInput = True
                except IndexError as e:
                     print(e)
                     error = True
                     validInput = False
                     engine.say("problem in reading your tag, please enter your answer again")
                     engine.runAndWait()
                while(error == True):
                    ans = answerInput()
                    try:
                        if(ans[0:2] == "P1" or ans[0:2] == "P2" or ans[0:2] == "P3" or ans[0:2] == "P4"):
                            print(ans[2])
                            print('run try block2')
                            validInput = True
                            error = False
                    except IndexError as e:
                        print(e)
                        error = True
                        validInput = False
                        engine.say("problem in reading your tag, please enter your answer again")
                        engine.runAndWait()
                
            if(validInput == True):
                engine.say("You have selected option " + ans[2])
                engine.say("Are you sure, Do you want to lock option " + ans [2])
                engine.runAndWait()
                ans = answerInput()
                time.sleep(1)
                engine.say("Your final answer is option"+ans[2])
                engine.runAndWait() 
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
                   updateScore(players[i],points,noOfPlayers)
                elif(realAns == q['answer'] and (str(i+1) != ans[1])):
                   engine.say('Your answer is right but player ' + str(i+1) + 'did not give this answer. No points to player'+ str(i+1))
                else:
                    engine.say('Your answer is wrong')
                
                for y in playerScores:
                    print("player: " + str(y))
               
                i=i+1

            if(i==noOfPlayers):
                
                engine.say('After ' + str(rounds) + 'rounds score is  ')
                rounds+=1
                for x in range(0,noOfPlayers):
                    engine.say('Player '+str(x+1) +' '+ str(playerScores[x]) + ' points.')
                    engine.runAndWait()
                i=0
            if rounds==4:
                print(rounds)
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
                engine.say("Do you want to play again? To play again place card of any player, to end game place end game card")
                engine.runAndWait()
                print("do you want to paly again?")
                playAgain = answerInput()
                if(playAgain[0:2] == "EG"):
                  engine.say("Are you sure you want to end the game. If you want to end game then place End Game card again ")
                  engine.runAndWait()
                  endGame = True
                  newGame = False
                if(playAgain[0:2] == "P1" or playAgain[0:2] == "P3" or playAgain[0:2] == "P3" or playAgain[0:2] == "P4"):
                  newGame = True
                if(endGame == True):  
                  playAgain = answerInput()
                  if(playAgain[0:2] == "EG"): 
                     rpiHalt = True
                     newGame = False
                     startGame = False
                     shutdownRpi(rpiHalt)
                  if(playAgain[0:2] == "P1" or playAgain[0:2] == "P3" or playAgain[0:2] == "P3" or playAgain[0:2] == "P4"):
                    newGame = True
                    engine.say("Lets play again")
                    engine.runAndWait()

'''
            except IndexError as e:
                 print(e)
                 error = True
                 engine.say("problem in reading your tag, please enter your answer again")
                 engine.runAndWait() 
                 while(error == True):
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
            
                     if(ans == "EndGame"):
                         print("Confirm??")
                         enagine.say("Are you sure you want to end game, to end game place end game card again,  if you place that card by mistake then place card of any player to continue the game")
                         engine.runAndWait()
                         end = answerInput()
                         if(end == "EndGame"):
                            areYousure = True
                     if(ans == "GameRules"):
                         readRules()
                         enagine.say("Enter you answer")
                         engine.runAndWait()
                         ans = answerInput()
                     try:
                          if(ans[0:2] == "P1" or ans[0:2] == "P2" or ans[0:2] == "P3" or ans[0:2] == "P4"):
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
                             eroor = False
                             '''
