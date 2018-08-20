import pyttsx3;
import json
import requests
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)
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
})'''
'''
with open('quizQuestions.txt', 'w') as outfile:  
    json.dump(quizQuestions, outfile)
'''
with open('quizQuestions.txt') as json_file:
    data = json.load(json_file)
    for q in data['questionBank']:
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
        print('answer is : ' + q['answer'])
        engine.say('answer is : ' + q['answer'])
        engine.runAndWait()
