import time
# Input
def inputInt(prompt):
    allowedChar = "-0123456789"
    while True:
        userInput = input(prompt)
        if all(char in allowedChar for char in userInput):
            return userInput
        else:
            print("[ERROR] Invalid input! Please enter an integer")
            
numberStart = int(inputInt("Number with which to start the search: "))
numberEnd = int(inputInt("Number to stop the search with: ")) 
primesToFind = int(inputInt("Amount of prime numbers to find: "))

# Definition
start_time = time.time()
primesStillToFind = primesToFind

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numberToCheck = numberStart
numbersCheckingDone = 0

# Programm
while primesStillToFind > 0 and not numberEnd + 1 == numberToCheck:
    if isPrime(numberToCheck):
        print(f"{numberToCheck}")
        primesStillToFind -= 1
    numbersCheckingDone += 1
    numberToCheck += 1

primesPerSecond = numbersCheckingDone / (time.time() - start_time)
print("-----[ RESULTS ]-----")
print(f"{time.time() - start_time:.2f}s needed to find the first {primesToFind} prime numbers from {numberStart} to {numberEnd}. That is {primesPerSecond:.4f} primes per second.")

