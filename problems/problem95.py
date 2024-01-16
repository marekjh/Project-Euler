from primes import divisors

N = 1_000_000
seen = set()
max_length = 0
for n in range(2, N):
    if n in seen:
        continue
    chain = []
    while True:
        chain.append(n)
        seen.add(n)
        factors = divisors(n) - {n}
        n = sum(factors)
        if n in chain:
            i = chain.index(n)
            if n in chain and len(chain) - i > max_length:
                max_length = len(chain) - i
                max_chain = chain[i:]
            break
        if n in seen or n >= N:
            break

print(min(max_chain))

