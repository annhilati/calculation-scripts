from python import Python
from math import pow
import time as Time


fn isPrime(num: Int) -> Bool:
    if num < 2:
        return False
    for i in range(2, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            return False
    return True


fn inputInt(prompt: String) raises -> Int:
    var py = Python.import_module("builtins")
    while True:
        var userInput: String = str(py.input(prompt))
        try:
            return int(userInput)
        except:
            print("[ERROR] Invalid input! Please enter an integer")


fn main() raises:

    var numberStart: Int = inputInt("Number with which to start the search: ")
    var numberEnd: Int = inputInt("Number to stop the search with: ")
    var primesToFind: Int = inputInt("Amount of prime numbers to find: ")

    # Definition
    var primesStillToFind = primesToFind

    var numberToCheck = numberStart
    var numbersCheckingDone = 0

    while primesStillToFind > 0 and not numberEnd + 1 == numberToCheck:
        if isPrime(numberToCheck):
            print(numberToCheck)
            primesStillToFind -= 1
        numbersCheckingDone += 1
        numberToCheck += 1

    print("-----[ RESULTS ]-----")
    #print(f"{time.time() - start_time:.2f}s needed to find the first {primesToFind} prime numbers from {numberStart} to {numberEnd}. That is {primesPerSecond:.4f} primes per second.")
    print("Found the first", primesToFind, "prime numbers from", numberStart, "to", numberEnd)