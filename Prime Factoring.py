def inputPosInt(prompt: str) -> int:
    while True:
        userInput = input(prompt)
        try:
            temp = int(userInput)
            if temp > 0:
                return temp
        except:
            print("  ║ [ERROR] Invalid input! Please enter an integer")

def isPrime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isInteger(number: float | int) -> bool:
    if number % 1 == 0:
        return True
    else:
        return False

#print(isInteger(5))

while True:
    dividers: list = []
    primefactors: list = []

    print(f"╔════════════════════════════════════════════════════════════════════╗")
    print(f"║ What number do you want to factorize?                              ║")
    print(f"╚═╦══════════════════════════════════════════════════════════════════╝")
    number: int = inputPosInt(f"  ║ >>> ") 
    if isPrime(number):
        dividers.append(number)
    else:
        numberCalc = number
        for factorToTry in range(2, number + 1):
            while isInteger(numberCalc / factorToTry):
                primefactors.append(factorToTry)
                numberCalc = int(numberCalc / factorToTry)
            if numberCalc == 1:
                break


    print(primefactors) # Debug