def max_sum(N):
    M = 0
    for a in range(1, N):
        for b in range(1, N):
            digit_sum = sum([int(c) for c in str(a ** b)])
            if digit_sum > M:
                M = digit_sum
    return M

print(max_sum(100))