def factorial(n: int):
    out: int = 1
    for i in range(1, n + 1):
        out *= i
    return out

def binominal_coefficient(n: int, k: int):
    return factorial(n) / (factorial(k) * factorial(n - k))

def binominal_distribution(n: int, k: int, p: float):
    return binominal_coefficient(n, k) * (p ** k) * ((1-p) ** (n - k))


def bdf_exact(n: int, k: int, p: float): # Funktioniert definitiv
    return binominal_distribution(n, k, p)
def bdf_max(n: int, k_max: int, p: float): # Funktioniert definitiv
    out: float = 0
    for i in range(0, k_max + 1):
        out = out + binominal_distribution(n, i, p)
    return out
def bdf_min(n: int, k_min: int, p: float): # Funktioniert nicht
    return 1 - binominal_distribution(n, k_min - 1, p)
def bdf_morethan(n: int, k_morethan: int, p: float): # Funktioniert definitiv
    return 1 - bdf_max(n, k_morethan, p)
def bdf_lessthen(n: int, k_lessthen: int, p: float):
    return 1 - bdf_min(n, k_lessthen, p)

n: int = 12
k: int = 3
p: float = 0.1

print(bdf_lessthen(n, k, p))