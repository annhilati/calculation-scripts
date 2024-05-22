import random

def inputInt(prompt):
    while True:
        userInput = input(prompt)
        try:
            return int(userInput)
        except:
            print("  ║ [ERROR] Invalid input! Please enter an integer")

def random_tests(iterations, list):
    for i in range(0, iterations):
        resultIt = random.randint(1, 6) + random.randint(1, 6)
        #print(f"  ║ {resultIt} wurde gewürfelt")
        list[resultIt - 1] = list[resultIt - 1] + 1

while True:
    print(f"╔════════════════════════════════════════════════════════════════════╗")
    print(f"║ Wie oft soll mit 2 Würfeln gewürfelt werden?                       ║")
    print(f"╚═╦══════════════════════════════════════════════════════════════════╝")
    iterationsReq = inputInt(f"  ║ >>> ") 

    print(f"╔═╩══════════════════════════════════════════════════════════════════╗")
    print(f"║ Zufallsversuche laufen...                                          ║")
    print(f"╚═╦══════════════════════════════════════════════════════════════════╝")
    results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    random_tests(iterationsReq, results)

    print(f"╔═╩══════════════════════════════════════════════════════════════════╗")
    print(f"║ Ergebnisse                                                         ║")
    print(f"╚═╦══════════════════════════════════════════════════════════════════╝")
    print(f"  ║ 2:  {'█' * int(results[1] / iterationsReq * 100)} {results[1]} ({(results[1] / iterationsReq * 100):.2f}%)")
    print(f"  ║ 3:  {'█' * int(results[2] / iterationsReq * 100)} {results[2]} ({(results[2] / iterationsReq * 100):.2f}%)")
    print(f"  ║ 4:  {'█' * int(results[3] / iterationsReq * 100)} {results[3]} ({(results[3] / iterationsReq * 100):.2f}%)")
    print(f"  ║ 5:  {'█' * int(results[4] / iterationsReq * 100)} {results[4]} ({(results[4] / iterationsReq * 100):.2f}%)")
    print(f"  ║ 6:  {'█' * int(results[5] / iterationsReq * 100)} {results[5]} ({(results[5] / iterationsReq * 100):.2f}%)")
    print(f"  ║ 7:  {'█' * int(results[6] / iterationsReq * 100)} {results[6]} ({(results[6] / iterationsReq * 100):.2f}%)")
    print(f"  ║ 8:  {'█' * int(results[7] / iterationsReq * 100)} {results[7]} ({(results[7] / iterationsReq * 100):.2f}%)")
    print(f"  ║ 9:  {'█' * int(results[8] / iterationsReq * 100)} {results[8]} ({(results[8] / iterationsReq * 100):.2f}%)")
    print(f"  ║ 10: {'█' * int(results[9] / iterationsReq * 100)} {results[9]} ({(results[9] / iterationsReq * 100):.2f}%)")
    print(f"  ║ 11: {'█' * int(results[10] / iterationsReq * 100)} {results[10]} ({(results[10] / iterationsReq * 100):.2f}%)")
    print(f"  ║ 12: {'█' * int(results[11] / iterationsReq * 100)} {results[11]} ({(results[11] / iterationsReq * 100):.2f}%)")
    print(f"  ╚══════════════════════════════════════════════════════════════════╝")
    input()
