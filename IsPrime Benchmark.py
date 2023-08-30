import time
# Eingabe
primesToFind = int(input("Prime numbers to find (the larger the number, the longer the benchmark takes and the more accurate it is): "))

# Definition
start_time = time.time()
primesStillToFind = primesToFind

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numberCalc = 1

# Programm
null = input("Start by pressing enter")
while primesStillToFind > 0:
    if is_prime(numberCalc):
        print(f"{numberCalc}")
        primesStillToFind = primesStillToFind - 1
    numberCalc = numberCalc + 1

primesPerSecond = primesToFind / (time.time() - start_time)
print("-------------------- RESULTS --------------------")
print(f"{time.time() - start_time:.2f}s needed to find the first {primesToFind} prime numbers. That is {primesPerSecond:.4f} primes per second.")

print(f"YOUR SCORE: {primesPerSecond * 10:.0f}   ! Note that the Score is dependent on in wich IDE you execute the benchmark !")