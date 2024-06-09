def sqrt_convergents(N):
    count = 0
    fraction = (3, 2)
    for _ in range(N):
        (n, d) = fraction
        if len(str(n)) > len(str(d)):
            count += 1
        fraction = (n + 2 * d, n + d)
    return count

print(sqrt_convergents(1000))

