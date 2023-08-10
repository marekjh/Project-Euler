from primes import factorize
from math import prod, floor

N = 50

def main():
    interior = 0
    for d in range(2, N+1):
        for n in range(1, d):
            rn, rd = reduce(n, d)
            interior += min((N-d)//rn, n//rd) + min(d//rn, (N-n)//rd)
    print(3*N**2 + floor(N**2/2) + 2*interior)

def reduce(a, b):
    a_factors = factorize(a)
    b_factors = factorize(b)
    shared = {x: min(a_factors.count(x), b_factors.count(x)) for x in set(a_factors).intersection(set(b_factors))}
    for factor, mult in shared.items():
        for _ in range(mult):
            a_factors.remove(factor)
            b_factors.remove(factor)
    return prod(a_factors), prod(b_factors)

main()