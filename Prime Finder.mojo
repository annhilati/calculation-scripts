from python import Python
from math import pow


fn isPrime(num: Int) -> Bool:
    if num < 2:
        return False
    for i in range(2, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            return False
    return True


def inputInt(prompt: String) -> Int:
    py = Python.import_module("builtins")
    allowedChar = "-0123456789"
    while True:
        statusOK = True
        userInput = py.input(prompt)
        #if all(char in allowedChar for char in userInput):
        for char in userInput:
            #print(char)
            if not str(char) in allowedChar:
                statusOK = False
        if statusOK == True:
            return int(userInput)
        else:
            print("[ERROR] Invalid input! Please enter an integer")


fn main() raises:
    var num = inputInt(">>> ")

    print(isPrime(num))