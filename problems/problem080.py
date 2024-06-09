def digit_sum(N, D):
    S = 0
    for n in range(2, N+1):
        if n**0.5 == int(n**0.5):
            continue

        curr = 0
        for p in range(D):
            for d in range(1, 10):
                new = 10*curr+d
                if new**2 > n*10**(2*p):
                    curr = new - 1
                    break
            else:
                curr = new
        S += sum(int(x) for x in str(curr))
    
    return S

print(digit_sum(100, 100))
