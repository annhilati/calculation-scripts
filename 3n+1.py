import time
# Eingabe
numberToBeginWith = int(input("Number to begin solving with for 3n+1: "))
numbersToSolve = int(input("Numbers to solve for 3n+1: "))
SolveTowardsMinus = False

# Programm
start_time = time.time()
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
        print(f"{time.time() - start_time:.2f}s: Number {numberToSolveFor} broke the record of {operationsRecord} operations which is now {operationsCalc}, {operationsDone} total operations so far")
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
print(f"Time needed:         {time.time() - start_time:.2f}s")
print(f"Numbers per second:  {numbersToSolve / (time.time() - start_time):.2f}")
print(" ")
print(f"Number with most calculations needed: (see last line of the log)")
