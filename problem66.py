from math import floor

def main():
    N = 1000
    max_x = 0
    for D in range(2, N + 1):
        if D ** 0.5 == int(D ** 0.5):
            continue
        x = convergent_numerator(terms(D))
        if x > max_x:
            max_x = x
            max_D = D
    print(max_D)

def convergent_numerator(terms):
    n, d = terms[-1], 1 
    for s in terms[-2::-1]:
        n, d = d, n
        n = s * d + n
    return n

def terms(n):
    root = n ** 0.5
    seen = set()
    period = 0
    a, d, m = floor(root), 1, 0
    a_list = [a]
    while True:
        m = d * a - m
        d = (n - m ** 2) / d
        a = floor((floor(root) + m) / d)
        a_list.append(a)
        if (a, d, m) in seen:
            break
        seen.add((a, d, m))
        period += 1
    if period % 2 == 0:
        return a_list[:-1]
    return a_list + a_list[1:-1]

main()
