N = 100
sequence = [2]

for n in range(N - 1):
    if n % 3 == 1:
        sequence.append(2 * ((n - 1) / 3 + 1))
    else:
        sequence.append(1)

n, d = sequence[-1], 1 
for s in sequence[-2::-1]:
    n, d = d, n
    n = s * d + n

print(sum(int(x) for x in str(int(n))))
