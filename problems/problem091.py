from math import floor

N = 50

def main():
    interior = 0
    for d in range(2, N+1):
        for n in range(1, d):
            rn, rd = reduce(n, d)
            interior += min((N-d)//rn, n//rd) + min(d//rn, (N-n)//rd)
    print(3*N**2 + floor(N**2/2) + 2*interior)

def reduce(a, b):
    shared = gcd(a, b)
    return a//shared, b//shared

def gcd(x, y):
    x, y = tuple(sorted([x, y], reverse=True))
    while y != 0:
        x, y = y, x % y
    return x



main()