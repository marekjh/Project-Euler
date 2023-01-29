from math import factorial

def selections_greater_than(N):
    n = 2
    product = 1
    while True:
        product *= n
        if product > N:
            start = n
            break
        n += 1
    
    count = 0
    for n in range(start, 101):
        for r in range(1, n + 1):
            nCr = factorial(n) / (factorial(r) * factorial(n - r))
            if nCr > N:
                count += 1
    return count

print(selections_greater_than(1_000_000))