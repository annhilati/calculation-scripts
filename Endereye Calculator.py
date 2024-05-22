def factorial(n: int):
    out: int = 1
    for i in range(1, n + 1):
        out *= i
    return out

def binomial_coefficient(n: int, k: int):
    return factorial(n) / (factorial(k) * factorial(n - k))
def binomial_distribution(n: int, k: int, p: float):
    return binomial_coefficient(n, k) * (p ** k) * ((1-p) ** (n - k))


def bdf_exact(n: int, k: int, p: float): # Funktioniert definitiv
    return binomial_distribution(n, k, p)
def bdf_max(n: int, k_max: int, p: float): # Funktioniert definitiv
    out: float = 0
    for i in range(0, k_max + 1):
        out = out + binomial_distribution(n, i, p)
    return out
def bdf_min(n: int, k_min: int, p: float):
    return 1 - bdf_max(n, k_min - 1, p)
def bdf_morethan(n: int, k_morethan: int, p: float): # Funktioniert definitiv
    return 1 - bdf_max(n, k_morethan, p)
def bdf_lessthen(n: int, k_lessthen: int, p: float):
    return bdf_max(n, k_lessthen - 1, p)

def inputInt(prompt):
    while True:
        userInput = input(prompt)
        try:
            return int(userInput)
        except:
            print("[ERROR] Invalid input! Please enter an integer")

print("╔════════════════════════════════════════════════════════════════════╗")
print("║ Please enter an amount of Endereyes in a End-Portal                ║")
print("╚═╦══════════════════════════════════════════════════════════════════╝")
endereyes = int(inputInt("  ║ >>> "))
print(f"╔═╩══════════════════════════════════════════════════════════════════╗")
print(f"║ Probabilities are beeing calculated ...                            ║")
print(f"╚═╦══════════════════════════════════════════════════════════════════╝")
n: int = 12
k: int = endereyes
p: float = 0.1
print(f"  ║ n = {n}")
print(f"  ║ k = {k}")
print(f"  ║ p = {p}")
print(f"╔═╩══════════════════════════════════════════════════════════════════╗")
print(f"║ Probabilities per naturally occuring End-Portal:                   ║")
print(f"╚═╦══════════════════════════════════════════════════════════════════╝")
print(f"  ║ Exactly {k} Endereyes ≈ {bdf_exact(n, k, p):.4f}% of EPs")
print(f"  ║ Minimum {k} Endereyes ≈ {bdf_min(n, k, p):.4f}% of EPs")
print(f"  ║ Maximum {k} Endereyes ≈ {bdf_max(n, k, p):.4f}% of EPs")
print(f"  ║ More than {k} Endereyes ≈ {bdf_morethan(n, k, p):.4f}% of EPs")
print(f"  ║ Less than {k} Endereyes ≈ {bdf_lessthen(n, k, p):.4f}% of EPs")
print(f"  ╚══════════════════════════════════════════════════════════════════╝")