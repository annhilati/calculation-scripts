# Config
minNum = 0
maxNum = 10

# System
from random import randint
def inputPosInt(prompt):
    allowedChar = "0123456789"
    while True:
        userInput = input(prompt)
        if all(char in allowedChar for char in userInput):
            return int(userInput)
        else:
            print("Du Idiot! Ich habe eine Ganzzahl gewählt! Versuchs nochmal!")    
def inputYN(promt):
    allowedChar = "ynYN"
    while True:
        userInput = input(promt)
        if all(char in allowedChar for char in userInput) and len(userInput) == 1:
            if userInput == "y" or userInput == "Y":
                return True
            else:
                return False
        else:
            print("Bitte gib \"y\" oder \"n\" für yes und no an.")

# Programm
anotherGame = True
while anotherGame == True:
    numGuess = -1
    numRandom = randint(minNum, maxNum)
    guesses = []
    print("Ich habe eine Zahl gewählt.")
    while numGuess != numRandom:
        numGuess = int(inputPosInt("Rate, welche Zahl ich gewählt hab! "))
        if numGuess in guesses:
            print("Digga du hast das schonmal geraten...")
        elif numGuess < minNum or numGuess > maxNum:
            print(f"Bro, meine Zahl liegt irgendwo zwischen {minNum} und {maxNum}...")
        elif numGuess != numRandom:
            print("Bist du so dumm wie du aussiehst? Falsch geraten!")
        else:
            print(f"Gut gemacht, du Atze! Meine Zahl war in der Tat {numRandom}")
        guesses.append(numGuess)
    anotherGame = inputYN("Willst du nochmal spielen? [Y/N] ")
    print(" ")
print("Spiel beendet")
