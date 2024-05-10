from python import Python
import time
from math import round, pow

fn inputInt(prompt: String) raises -> Int:
    var py = Python.import_module("builtins")
    while True:
        var userInput: String = py.input(prompt)
        try:
            return int(userInput)
        except:
            print("  ║ [ERROR] Invalid input! Please enter an integer")

fn round_float(value: Float16, decimals: Int) -> Float16:
    var multiplier: Int = 10 ** decimals
    return int(value * multiplier) / multiplier

fn main() raises:
    var time = Python.import_module("time")

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

    var TimeStart = time.time()

    print("╔═╩══════════════════════════════════════════════════════════════════╗")
    print("║ Beginning Calculating...                                           ║")
    print("╚═╦══════════════════════════════════════════════════════════════════╝")

    while iterationsStill > 0:
        var opsCalc: Int = 0

        var x: Int = numberIteration
        while not x == 1 or 0 or -1 or -5 or -17:
            if x % 2 == 1:
                x = x * 3 + 1
            else:
                x = int(x / 2) # Gibt sonst Error
            opsCalc = opsCalc + 1

        opsDone = opsDone + opsCalc
        if opsCalc > opsRecord:
            var timestamp = time.time() - TimeStart
            #print('  ║ ', timestamp, 'Number', numberIteration, 'broke the record of', opsRecord, 'operations which now is', opsCalc)
            print('  ║ Number', numberIteration, 'broke the record of', opsRecord, 'operations which now is', opsCalc)
            opsRecord = opsCalc

        iterationsStill = iterationsStill - 1
        numberIteration = numberIteration + 1

    #var timeNeeded = time.time() - TimeStart
    var timeNeeded = round_float(Float16(time.time() - TimeStart), 2)
    var numbersPerSecond = iterationsRequested / (time.time() - TimeStart)

    print("╔═╩══════════════════════════════════════════════════════════════════╗")
    print("║ Results                                                            ║")
    print("╚═╦══════════════════════════════════════════════════════════════════╝")
    print("  ║ Numbers solved:      ", numberBegin, "to", numberIteration)
    print("  ║ Time needed:         ", timeNeeded, "seconds")
    print("  ║                      ", timeNeeded / 60.0, "minutes")
    print("  ║ Numbers per second:  ", numbersPerSecond)
    print("  ║  ")
    print("  ║ Number with most calculations needed: (see last line of the log)")
    print("  ╚══════════════════════════════════════════════════════════════════╝")

