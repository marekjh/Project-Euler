from math import floor, ceil

def main():
    N = 12_000
    upper = 1/2
    lower = 1/3

    total = 0
    for d in range(2, N + 1):
        for n in range(ceil(d * lower), floor(d * upper) + 1):
            frac = n / d
            if frac == upper or frac == lower:
                continue
            if gcd(n, d) == 1:
                total += 1
    print(total)

def gcd(x, y):
    tmp = (x, y)
    x, y = max(tmp), min(tmp)
    while y != 0:
        x, y = y, x % y
    return x

main()