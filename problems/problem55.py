def lychel_nums(N):
    count = 0
    for n in range(1, N):
        for _ in range(50):
            n = n + int(str(n)[::-1])
            if str(n) == str(n)[::-1]:
                break
        else:
            count += 1
    return count

print(lychel_nums(10_000))