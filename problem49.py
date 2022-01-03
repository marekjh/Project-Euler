def sequence():
    primes = generate_primes()
    for n in range(1488, 10_000):
        for k in range(1, int(((10_000 - n) / 2))):
            seq = [n, n + k, n + 2 * k]
            for val in seq:
                if not is_prime(val, primes):
                    break
            else:
                seq = [str(x) for x in seq]
                if set(seq[0]) == set(seq[1]) == set(seq[2]):
                    return seq[0] + seq[1] + seq[2]

def generate_primes():
    primes = [2, 3]
    for n in range(5, int(1_000_000 ** 0.5) + 10, 2):
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

print(sequence())

#https://projecteuler.net/problem=49