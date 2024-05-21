from scipy.stats import binom

def probability_of_success(n, k, p):
    # Kumulative Wahrscheinlichkeit für weniger als k Erfolge
    prob_less_than_k = binom.cdf(k - 1, n, p)
    # Wahrscheinlichkeit für k oder mehr Erfolge
    prob_at_least_k = 1 - prob_less_than_k
    return prob_at_least_k

n = 10  # Anzahl der Versuche
k = 1   # Mindestanzahl an Erfolgen
p = 1 / 6  # Erfolgswahrscheinlichkeit

print("Wahrscheinlichkeit, mindestens", k, "Erfolge in", n, "Versuchen zu haben:", probability_of_success(n, k, p))
