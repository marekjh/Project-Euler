def generate_primes(N):
    N **= 2
    primes = [2, 3]
    for n in range(5, int(N ** 0.5) + 10, 2):
        i = 0
        while primes[i] <= int(n ** 0.5):
            if n % primes[i] == 0:
                break
            i += 1
        else:
            primes.append(n)
    return primes

def is_prime(n, p):
    print(n)
    i = 0
    while p[i] <= int(n ** 0.5):
        if n % p[i] == 0:
            return False
        i += 1
    return True
