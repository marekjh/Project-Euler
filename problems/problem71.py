from primes import factorize
from math import floor, ceil

def main():
    N = 1_000_000
    upper = 3/7
    lower = 2/5
    max_val = 0

    for d in range(12, N + 1):
        for n in range(ceil(d * lower), floor(d * upper) + 1):
            val = n / d
            if val == upper:
                continue
            if val > max_val:
                max_val = val
                lower = val
                min_fraction = (n, d)
    print(reduce(*min_fraction))

def reduce(n, d):
    n_factors = factorize(n)
    d_factors = factorize(d)
    for f in n_factors:
        if f in d_factors:
            n_factors.remove(f)
            d_factors.remove(f)
    return product(n_factors), product(d_factors)

def product(arr):
    product = 1
    for n in arr:
        product *= n
    return product

main()