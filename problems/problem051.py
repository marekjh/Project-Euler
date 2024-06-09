from itertools import combinations

def generate_primes():
    primes = [2, 3]
    for n in range(5, 200_000, 2):
        i = 0
        while primes[i] <= int(n ** 0.5):
            if n % primes[i] == 0:
                break
            i += 1
        else:
            primes.append(n)
    return primes

def is_prime(n, p):
    i = 0
    while p[i] <= int(n ** 0.5):
        if n % p[i] == 0:
            return False
        i += 1
    return True

def check():
    primes = generate_primes()
    for p in [n for n in primes if n > 56_003]:
        length = len(str(p))
        for i in range(1, length):
            for combo in combinations(range(length), i):
                count = 0
                for j in range(1, 10):
                    iter_p = list(str(p))
                    for k in combo:
                        iter_p[k] = str(j)
                    current_iter = int("".join(iter_p))
                    if is_prime(current_iter, primes):
                        if count == 0:
                            candidate = current_iter
                        count += 1
                    if count == 8:
                        return candidate

print(check())
                

