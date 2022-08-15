from problem69 import phi

def main():
    N = 1_000_000

    total = 0
    for d in range(2, N + 1):
        total += phi(d)
    print(total)

main()