from math import sqrt

def inputRealNotZero(prompt):
    while True:
        userInput = input(prompt)
        try:
            userInputConverted = float(userInput)
            if float(userInput) == 0.0:
                print("  ║ [ERROR] Ungültige Eingabe. Bei diesem Rechenvorgang darf keine Seite 0 sein.")
            else:
                return float(userInputConverted)
        except:
            print("  ║ [ERROR] Ungültige Eingabe. Bitte geben Sie nur eine Fließkommazahl mit \".\" als Dezimalkomma an.")

def v(sideVector):
    return sideVector[1]

print("╔════════════════════════════════════════════════════════════════════╗")
print("║ Geben Sie Daten für ein Dreieck an                                 ║")
print("║ Dieser Rechner verwendet A B C a b c. Bitte bedenken Sie dies      ║")
print("╠════════════════════════════════════════════════════════════════════╣")
print("║ Geben Sie die Seitenlänge von a an.                                ║")
print("╚═╦══════════════════════════════════════════════════════════════════╝")
sideA = inputRealNotZero("  ║ a <= ")
print("╔═╩══════════════════════════════════════════════════════════════════╗")
print("║ Geben Sie die Seitenlänge von b an.                                ║")
print("╚═╦══════════════════════════════════════════════════════════════════╝")
sideB = inputRealNotZero("  ║ b <= ")
print("╔═╩══════════════════════════════════════════════════════════════════╗")
print("║ Geben Sie die Seitenlänge von c an.                                ║")
print("╚═╦══════════════════════════════════════════════════════════════════╝")
sideC = inputRealNotZero("  ║ c <= ")

sides = [["a", sideA], ["b", sideB], ["c", sideC]]
sidesSorted = sorted(sides, key=lambda x: (x[1], x[0]))
#print("  ║ [DEBUG]", sidesSorted) # Debug

print(f"╔═╩══════════════════════════════════════════════════════════════════╗")
print(f"║ Daten werden geprüft...                                            ║")
print(f"╚═╦══╦═══════════════════════════════════════════════════════════════╝")
print(f"  ║  ║ Seite a: {sideA}")
print(f"  ║  ║ Seite b: {sideB}")
print(f"  ║  ║ Seite c: {sideC}")

if not v(sidesSorted[2]) <= v(sidesSorted[0]) + v(sidesSorted[1]):
    print("  ║ [COMMENT] Die Seiten ergeben kein gültiges Dreieck")
else:
    # Ist ein Dreieck
    print("  ║ [COMMENT] Die Seiten ergeben ein gültiges Dreieck")

    if v(sidesSorted[2]) ** 2 == v(sidesSorted[0]) ** 2 + v(sidesSorted[1]) ** 2:
        print(f"  ║ [COMMENT] Das Dreieck ist pythagoräisch")
        print(f"  ║  ║ Die Hypothenuse ist {sidesSorted[2][0]}")
    
    s = (sideA + sideB + sideC) / 2
    area = sqrt(s * (s - sideA) * (s - sideB) * (s - sideC))

    print(f"  ║ Die Fläche beträgt {area}")
