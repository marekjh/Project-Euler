from math import factorial

def main():
    N = 1_000_000
    seq_length = 60
    factorials = [factorial(x) for x in range(10)]
    seen = set()
    count = 0

    for n in range(1, N):
        seq = set()
        if n in seen:
            continue
        current = n
        while current not in seq:
            seq.add(current)
            seen.add(current)
            current = sum(factorials[int(x)] for x in str(current))
        if len(seq) == seq_length:
            count += 1
    print(count)

main()

