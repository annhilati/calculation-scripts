import time
# Eingabe
numberToBeginWith = int(input("Number to begin solving with for 3n+1: "))
numbersToSolve = int(input("Numbers to solve for 3n+1: "))
SolveTowardsMinus = False

# Programm
start_time = time.time()
numberToSolveFor = numberToBeginWith
numbersStillToSolve = numbersToSolve
operationsDone = 0
operationsRecord = 0

while numbersStillToSolve > 0: # and numberToSolveFor >= numberToBeginWith:
    numberCalc = numberToSolveFor
    operationsCalc = 0
    while numberCalc != 1 and numberCalc != 0 and numberCalc != -1 and numberCalc != -5 and numberCalc != -17:
        if numberCalc % 2 == 1:
            numberCalc = numberCalc * 3 + 1
            operationsCalc = operationsCalc + 1
        else:
            numberCalc = numberCalc / 2
            operationsCalc = operationsCalc + 1
    # Schreibt neue Rekorde in die Konsole        
    if operationsCalc > operationsRecord:
        print(f"{time.time() - start_time:.2f}s: Number {numberToSolveFor} broke the record of {operationsRecord} operations and is now {operationsCalc}, {operationsDone} total operations so far")
        operationsRecord = operationsCalc
    operationsDone = operationsDone + operationsCalc
    # Gibt an, welche Zahl als nächstes gelöst wird
    numbersStillToSolve = numbersStillToSolve - 1
    if SolveTowardsMinus == False:
        numberToSolveFor = numberToSolveFor + 1
    else:
        numberToSolveFor = numberToSolveFor - 1

# Ausgabe
if SolveTowardsMinus == False:
   print(f"Done, solving for numbers from {numberToBeginWith} to {numberToBeginWith+numbersToSolve}")
else:
   print(f"Done, solving for numbers from {numberToBeginWith} to {numberToBeginWith-numbersToSolve}")

