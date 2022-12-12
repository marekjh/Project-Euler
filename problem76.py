import numpy as np
N = 100

poly = np.poly1d([1])
for n in range(1, N + 1):
    new = np.poly1d([1 if x % n == 0 else 0 for x in range(N + 1)][::-1])
    poly = np.polymul(poly, new)
print(poly.c[-(N + 1)] - 1) # Don't include the partition containing just 100 itself, needs at least two integers