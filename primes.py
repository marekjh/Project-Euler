import pickle

with open("primes.pickle", "rb") as f:
    PRIMES = pickle.load(f)

def generate_primes(N):
    primes = [2, 3]
    for n in range(5, N, 2):
        i = 0
        while primes[i] <= int(n ** 0.5):
            if n % primes[i] == 0:
                break
            i += 1
        else:
            primes.append(n)
    return primes

def is_prime(n):
    return n in PRIMES
