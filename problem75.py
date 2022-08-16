from itertools import combinations_with_replacement

def main():
    N = 1_500_000

    print(sum(1 for L in range(12, N + 1, 2) if singular(L)))

def divisors(n):
    divisors = set()
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            divisors.add(x)
            divisors.add(n // x)
    return divisors

def singular(n):
    products = set()
    for (a, b) in combinations_with_replacement(divisors(n), 2):
        prod = a * b
        if (n ** 2 / 2) % prod == 0 and prod > n / 2 and prod < n:
            products.add(prod)
    return len(products) == 2

if __name__ == "__main__":
    main()