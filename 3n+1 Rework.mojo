from python import Python

fn inputInt(prompt: String) raises -> Int:
    var py = Python.import_module("builtins")
    while True:
        var userInput: String = py.input(prompt)
        try:
            return int(userInput)
        except:
            print("  ║ [ERROR] Invalid input! Please enter an integer")

fn main() raises:
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║ Please enter a number to start the solvation                       ║")
    print("╚═╦══════════════════════════════════════════════════════════════════╝")
    var numberBegin: Int = inputInt("  ║ >>> ")
    print("╔═╩══════════════════════════════════════════════════════════════════╗")
    print("║ Please enter the amount of iterations to be done                   ║")
    print("╚═╦══════════════════════════════════════════════════════════════════╝")
    var iterationsRequested: Int = inputInt("  ║ >>> ")

    var numberIteration: Int = numberBegin
    var iterationsStill: Int = iterationsRequested
    var opsDone: Int = 0 
    var opsRecord: Int = -1 

    print("╔═╩══════════════════════════════════════════════════════════════════╗")
    print("║ Beginning Calculating...                                           ║")
    print("╚═╦══════════════════════════════════════════════════════════════════╝")

    while iterationsStill > 0:
        print("Debug 1")
        var opsCalc: Int = 0

        var x: Int = numberIteration
        while x != 1 or 0 or -1 or -5 or -17:
            if x % 2 == 1:
                print("Debug 2", x)
                x = x * 3 + 1
            else:
                print("Debug 3", x)
                x = int(x / 2) # Gibt sonst Error
            opsCalc = opsCalc + 1

        print("Debug 4")
        opsDone = opsDone + opsCalc
        if opsCalc > opsRecord:
            print('  ║ Number', numberIteration, 'broke the record of', opsRecord, 'operations which now is', opsCalc)
            opsRecord = opsCalc

        iterationsStill = iterationsStill - 1
        numberIteration = numberIteration + 1