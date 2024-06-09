def find_x(M):
    p = 1
    while True:
        for x in range(10 ** p, 10 ** (p + 1) // M):
            x_digits = set(str(x))
            for m in range(2, M + 1):
                if set(str(m * x)) != x_digits:
                    break
            else:
                return x
        p += 1

print(find_x(6))