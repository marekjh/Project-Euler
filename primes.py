import pickle

with open("primes.pickle", "rb") as f:
    PRIMES = pickle.load(f)
SORTED_PRIMES = sorted(list(PRIMES))

def generate_primes(N):
    primes = [2, 3]
    for n in range(5, N, 2):
        i = 0
        p = 2
        while p <= int(n ** 0.5):
            if n % p == 0:
                break
            i += 1
            p = primes[i]
        else:
            primes.append(n)
    return primes

def is_prime(n):
    return n in PRIMES

def factorize(n):
    return factorize_helper(n, [])

def factorize_helper(n, factors):
    i = 0
    p = 2
    while p <= int(n ** 0.5):
        if n % p == 0:
            return factorize_helper(n // p, factors + [p])
        i += 1
        p = SORTED_PRIMES[i]
    return factors + [n]
    
    
def factorize2(n):
    factors = []
    while True:
        i = 0
        p = 2
        while p <= int(n ** 0.5):
            if n % p == 0:
                factors.append(p)
                n //= p
                break
            i += 1
            p = SORTED_PRIMES[i]
        else:
            return factors + [n]
