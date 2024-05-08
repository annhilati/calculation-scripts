from python import Python

fn inputInt(prompt: String) raises -> Int:
    var py = Python.import_module("builtins")
    while True:
        var userInput: String = py.input(prompt)
        try:
            return int(userInput)
        except:
            print("[ERROR] Invalid input! Please enter an integer")

fn main() raises:
    var numberToBeginWith:Int = inputInt("[INPUT] Number to begin solving with for 3n+1: ")
    var numbersToSolve: Int = inputInt("[INPUT] Numbers to solve for 3n+1: ")
    var SolveTowardsMinus: Bool = False


    # Programm
    if SolveTowardsMinus == True:
        print("[INFO]  Numbers will be solved towards negative infinity until the specified calculations have been completed")
    else:
        print("[INFO]  Numbers will be solved towards positive infinity until the specified calculations have been completed")

    var numbersStillToSolve: Int = numbersToSolve
    var operationsDone: Int = 0
    var operationsRecord: Int = -1

    var numberToSolveFor: Int = numberToBeginWith

    while numbersStillToSolve > 0:
        var numberCalc: Int = numberToSolveFor
        var operationsCalc: Int = 0
        while numberCalc != 1 and numberCalc != 0 and numberCalc != -1 and numberCalc != -5 and numberCalc != -17:
            if numberCalc % 2 == 1:
                numberCalc = numberCalc * 3 + 1
            else:
                var numberCalc = numberCalc / 2
            operationsCalc = operationsCalc + 1

        # Schreibt neue Rekorde in die Konsole
        operationsDone = operationsDone + operationsCalc
        if operationsCalc > operationsRecord:
            print("Number", numberToSolveFor, "broke the record of", operationsRecord, "operations which is now", operationsCalc, ",", operationsDone, "total operations so far")
            operationsRecord = operationsCalc

        # Gibt an, welche Zahl als nächstes gelöst wird
        numbersStillToSolve = numbersStillToSolve - 1
        if SolveTowardsMinus == False:
            numberToSolveFor = numberToSolveFor + 1
        else:
            numberToSolveFor = numberToSolveFor - 1

    print("--------[ RESULTS ]--------")
    print("Numbers solved:      ", numberToBeginWith, " to ", numberToSolveFor)
    print(" ")
    print("Number with most calculations needed: (see last line of the log)")
