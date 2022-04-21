from json import load

with open('wordle.json') as file:
    data = load(file)
    edictionary = list(data.keys())

global alphabet
alphabet = list("abcdefghiklmnopqrstuvwxyz")

def wordExists(word):
    if word in edictionary:
        return(True)
    else:
        return(False)

def getLetters():
    wordle = []
    yellows = []
    greys = []
    for pos in range(1,6):
        letter = ":("
        while(letter not in alphabet and letter != "-"):
            letter = input("enter letter in position " + str(pos) + " (press - if unknown)\n").lower()
        if letter not in alphabet:
            wordle.append("-")
        else:
            wordle.append(letter)
    
    letter = "-"
    while(letter != "."):
        letter = input("enter a letter that you don't know the position for but is included(?) (enter . if you're done)\n").lower()
        if letter in alphabet != ".":
            yellows.append(letter)

    letter = "-"
    while(letter != "."):
        letter = input("enter a letter that's not included (enter . if you're done)\n").lower()
        if letter in alphabet != ".":
            greys.append(letter)

    return(wordle, yellows, greys)

def findWords(wordle, yellows, greys):
    indices = [i for i, char in enumerate(wordle) if char != "-"]
    wordList = []

    if len(indices) == 5:
        return(edictionary)
    
    for word in edictionary:
        valid = True
        for index in indices:
            if word[index] != wordle[index]:
                valid = False
        for char in yellows:
            if char not in word:
                valid = False
        for char in greys:
            if char in word:
                valid = False
        
        if valid:
            wordList.append(word)

    return(wordList)

wordleData = getLetters()
finalWords = findWords(wordleData[0], wordleData[1], wordleData[2])
for i in finalWords:
    print(i)