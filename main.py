import csv
import random
import json

aineet = {}
corrects = {}

try:
    with open('saved.json') as file:
        data = json.load(file)
        corrects = data
except:
    print('no saved data')

with open('alkuaineet.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        aineet[row[0]] = {'name': row[1], 'group': row[2]}
        corrects[row[0]] = 0

def getLowestList():
    lowest = None
    out = {}
    for symb, count in corrects.items():
        if lowest == None or count < lowest:
            lowest = count

    for symb, count in corrects.items():
        if  count == lowest:
            out[symb] = aineet[symb]
    return out

def askname(symb, obj):
    answerName = input('? Minkä alkuaineen merkki on '+symb+': ')
    if answerName.lower() == obj['name'].lower():
        print('✓ Oikein')
        return True
    else:
        print('✗ Väärin, olisi ollut '+obj['name'])
        return False

def askgroup(symb, obj):
    answerName = input('? Entä mikä on alkuaineen '+symb+' ryhmä: ')
    if answerName.lower() == obj['group'].lower():
        corrects[symb] += 1
        save()
        print('✓ Oikein, mennyt oikein '+str(corrects[symb])+' kertaa')
        return True
    else:
        print('✗ Väärin, olisi ollut '+obj['group'])
        return False

def save():
    with open('saved.json', 'w') as outfile:
        json.dump(corrects, outfile)

while True:
    lowestList = getLowestList()
    symb, obj = random.choice(list(getLowestList().items()))
    asktype = 'both'
    if asktype == 'both':
        if(askname(symb, obj)):
            askgroup(symb, obj)

