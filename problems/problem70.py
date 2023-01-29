from primes import SORTED_PRIMES
import math
import numpy as np
from itertools import combinations

def main():
    N = 10_000_000
    min_val = math.inf
    min_n = 0
    primes = np.array(SORTED_PRIMES)
    primes = primes[np.logical_and(primes > 1000, primes < 5000)] # centered around sqrt(10_000_000) ~ 3000
    for (p, q) in combinations(primes, 2):
            n = p * q
            if p == q or n >= N:
                continue
            phi_n = (p - 1) * (q - 1)
            val = n / phi_n
            if val < min_val and is_permutation(n, phi_n):
                min_val = val
                min_n = n
    print(min_n)

def is_permutation(a, b):
    a, b = str(a), str(b)
    return set(a) == set(b) and all(a.count(x) == b.count(x) for x in a)


main()