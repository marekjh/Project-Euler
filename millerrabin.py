import random

def is_prime(n, k):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = a**d % n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x**2 % n
            if x == n - 1:
                break
        else:
            return False
    return True

for n in range(100_000, 1_000_000):
    if is_prime(n, 40):
        print(n)