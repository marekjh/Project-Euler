n = 28433
for _ in range(7830457):
    n *= 2
    n %= 10**10
print(n + 1)