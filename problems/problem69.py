from primes import factorize

def main():
    N = 1_000_000
    max_val = 0
    max_n = 0

    for n in range(2, N + 1):
        val = n / phi(n)
        if val > max_val:
            max_val = val
            max_n = n
    print(max_n)

def phi(n):
    if n == 1:
        return 1
        
    phi = n
    for p in set(factorize(n)):
        phi *= (1 - 1 / p)
    return int(phi)
    
if __name__ == "__main__":
    main()