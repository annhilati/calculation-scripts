import time
# Eingabe
def inputInt(prompt):
    allowedChar = "-0123456789"
    while True:
        userInput = input(prompt)
        if all(char in allowedChar for char in userInput):
            return userInput
        else:
            print("[Error] Invalid input! Please enter an integer")
            
numberToBeginWith = int(inputInt("Number to begin solving with for 3n+1: "))
numbersToSolve = int(inputInt("Numbers to solve for 3n+1: "))
SolveTowardsMinus = False

# Programm
startTime = time.time()
numbersStillToSolve = numbersToSolve
operationsDone = 0
operationsRecord = -1

numberToSolveFor = numberToBeginWith

while numbersStillToSolve > 0: # and numberToSolveFor >= numberToBeginWith:
    numberCalc = numberToSolveFor
    operationsCalc = 0
    while numberCalc != 1 and numberCalc != 0 and numberCalc != -1 and numberCalc != -5 and numberCalc != -17:
        if numberCalc % 2 == 1:
            numberCalc = numberCalc * 3 + 1
        else:
            numberCalc = numberCalc / 2
        operationsCalc = operationsCalc + 1

    # Schreibt neue Rekorde in die Konsole
    operationsDone = operationsDone + operationsCalc
    if operationsCalc > operationsRecord:
        print(f"[{time.time() - startTime:.2f}s] Number {numberToSolveFor} broke the record of {operationsRecord} operations which is now {operationsCalc}, {operationsDone} total operations so far")
        operationsRecord = operationsCalc

    # Gibt an, welche Zahl als nächstes gelöst wird
    numbersStillToSolve = numbersStillToSolve - 1
    if SolveTowardsMinus == False:
        numberToSolveFor = numberToSolveFor + 1
    else:
        numberToSolveFor = numberToSolveFor - 1

# Ausgabe
print("--------[ RESULTS ]--------")
print(f"Numbers solved:      {numberToBeginWith} to {numberToSolveFor}")
print(f"Time needed:         {time.time() - startTime:.2f}s")
print(f"Numbers per second:  {numbersToSolve / (time.time() - startTime):.2f}")
print(" ")
print(f"Number with most calculations needed: (see last line of the log)")

