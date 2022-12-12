from itertools import permutations

# Digits present in all keys exclude 4 and 5
# None of the keys repeat digits, meaning almost certainly passcode contains no digit repeats
# So we try 8 digit passcodes using {0, 1, 2, 3, 6, 7, 8, 9}

def main():
    with open("keylog.txt") as f:
        keys = [x.strip() for x in f.readlines()]
    digits = {0, 1, 2, 3, 6, 7, 8, 9}

    for p in permutations(digits):
        if all(valid(k, p) for k in keys):
            print(p)
            break

def valid(k, p):
    k = [int(x) for x in k]
    return p.index(k[0]) < p.index(k[1]) < p.index(k[2])

main()

