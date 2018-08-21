import pyttsx3;
import json
import requests
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)
realAns = ""
players = [" player 1"," player 2"," player 3"," player 4"]
player1=0
player2=0
player3=0
player4=0
winner =""

f = open("quizGameRules.txt",'r')
gameRules = f.read()
engine.say(gameRules)
engine.runAndWait()
f.close()
'''
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(todos)
'''
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
'''
with open('quizQuestions.json', 'w') as outfile:  
    json.dump(quizQuestions, outfile)
'''

def updateScore(playerNum):
    if(playerNum == " player 1"):
        global player1
        player1 += 10
    if(playerNum == " player 2"):
        global player2
        player2 += 10
    if(playerNum == " player 3"):
        global player3
        player3 += 10
    if(playerNum == " player 4"):
        global player4
        player4 += 10
    
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
        
with open('quizQuestions.json') as json_file:
    data = json.load(json_file)
    i=0
    rounds = 0
    for q in data['questionBank']:
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
        engine.runAndWait()
        ans = input("enter your answer :")
        
        print('answer is : ' + q['answer'])
        if(ans == 'a'):
           realAns = q['a']
        if(ans == 'b'):
           realAns = q['b']
        if(ans == 'c'):
           realAns = q['c']
        if(ans == 'd'):
           realAns = q['d']   
        engine.say('answer is : ' + q['answer'])
        if(realAns == q['answer']):
           engine.say('Your answer is correct, 10 pointes to '+ players[i])
           updateScore(players[i])
        else:
            engine.say('Your answer is wrong')
        print(player1)
        print(player2)
        print(player3)
        print(player4)
        i=i+1
        if(i>3):
            i=0
            rounds+=1
            engine.say('After'+ str(rounds) + 'rounds score is.')
            engine.say('Player 1 '+ str(player1) + ' points.')
            engine.say('Player 2 '+ str(player2) + ' points.')
            engine.say('Player 3 '+ str(player3) + ' points.')
            engine.say('Player 4 '+ str(player4) + ' points.')
        engine.runAndWait()
        if rounds==3:
            engine.say('All rounds are over ')
            gameOver = winner(player1,player2,player3,player4)
            if(gameOver == True):    
               engine.say("Winner is "+ winner)
            if(winner == False):
                engine.say("Its a tie")
            engine.runAndWait()
            
 


