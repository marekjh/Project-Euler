import primes
import numpy as np
N = 100
min = 5000

prime_list = primes.SORTED_PRIMES
prime_list = prime_list[prime_list < N]
poly = np.poly1d([1])
for p in prime_list:
    new = np.poly1d([1 if x % p == 0 else 0 for x in range(N + 1)][::-1])
    poly = np.polymul(poly, new)
for i, c in enumerate(poly.c[::-1]):
    if c > min:
        print(i)
        break

