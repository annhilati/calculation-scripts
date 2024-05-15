from math import sqrt, acos, pi as pi

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

def degree(radian):
    return radian * (180 / pi)

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

sidesListed = [["a", sideA], ["b", sideB], ["c", sideC]]
sides = sorted(sidesListed, key=lambda x: (x[1], x[0]))
#print("  ║ [DEBUG]", sides) # Debug

print(f"╔═╩══════════════════════════════════════════════════════════════════╗")
print(f"║ Daten werden geprüft...                                             ")
print(f"║   a = {sideA}")
print(f"║   b = {sideB}")
print(f"║   c = {sideC}")
print(f"╚═╦══════════════════════════════════════════════════════════════════╝")

if not v(sides[2]) <= v(sides[0]) + v(sides[1]):
    print("  ║ [COMMENT] Die Seitenlängen ergeben kein gültiges Dreieck")
else:
    print("  ║ [COMMENT] Die Seiten ergeben ein gültiges Dreieck")
    print("  ║ ")

    # Fläche
    s = (sideA + sideB + sideC) / 2
    area = sqrt(s * (s - sideA) * (s - sideB) * (s - sideC))
    print(f"  ║ Fläche ≈ {area:.2f}")

    # Höhen
    heightA = (area * 2) / sideA
    heightB = (area * 2) / sideB
    heightC = (area * 2) / sideC
    print(f"  ║ Höhe auf a ≈ {heightA:.2f}")
    print(f"  ║ Höhe auf b ≈ {heightB:.2f}")
    print(f"  ║ Höhe auf c ≈ {heightC:.2f}")
    print(f"  ║")

    # Innenwinkel
    angleAlpha = degree(acos((sideB ** 2 + sideC ** 2 - sideA ** 2) / (2 * sideB * sideC)))
    angleBeta = degree(acos((sideA ** 2 + sideC ** 2 - sideB ** 2) / (2 * sideA * sideC)))
    angleGamma = degree(acos((sideA ** 2 + sideB ** 2 - sideC ** 2) / (2 * sideA * sideB)))
    print(f"  ║ α = ∠A ≈ {angleAlpha:.2f}°")
    print(f"  ║ β = ∠B ≈ {angleBeta:.2f}°")
    print(f"  ║ γ = ∠C ≈ {angleGamma:.2f}°")

    # Rechtwinkeleigenschaften
    if v(sides[2]) ** 2 == v(sides[0]) ** 2 + v(sides[1]) ** 2:
        print(f"  ║ [COMMENT] Das Dreieck ist rechtwinklig")
        print(f"  ║ Die Hypothenuse ist {sides[2][0]}")
    else: 
        print(f"  ║ [COMMENT] Das Dreieck hat keinen rechten Winkel")
