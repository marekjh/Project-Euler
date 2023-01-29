from math import floor

count = 0
for n in range(2, 10_000):
    root = n ** 0.5
    if root == int(root):
        continue
    seen = set()
    period = 0
    a, d, m = floor(root), 1, 0
    while True:
        m = d * a - m
        d = (n - m ** 2) / d
        a = floor((floor(root) + m) / d)
        if (a, d, m) in seen:
            break
        seen.add((a, d, m))
        period += 1
    if period % 2 == 1:
        count += 1

print(count)
        
