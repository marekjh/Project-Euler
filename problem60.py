from primes import PRIMES, is_prime
from itertools import combinations
import pickle

def main():
    first_primes = sorted(list(PRIMES))[:1000]
    pairs = {}

    for p in sorted(list(PRIMES)):
        s = str(p)
        for i in range(1, len(s)):
            first = s[:i]
            second = s[i:]
            if first.startswith("0") or second.startswith("0"):
                continue
            first, second = int(first), int(second)
            if is_prime(first) and is_prime(second) and is_prime(int(str(second) + str(first))):
                add_item(first, second, pairs)
                add_item(second, first, pairs)
    reduced_pairs = {k: v for k, v in pairs.items() if len(v) >= 4}

    candidates = []
    for p1 in first_primes:
        for p2 in first_primes:
            if p1 == p2 or not are_compatible(p1, p2) or p1 not in reduced_pairs or p2 not in reduced_pairs:
                continue
            likely = reduced_pairs[p1] & reduced_pairs[p2]
            for (p3, p4) in combinations(likely, 2):
                if are_compatible(p3, p4) and len({p1, p2, p3, p4}) == 4:
                    candidates.append([p1, p2, p3, p4])
    
    length_five = []
    for groups in [[reduced_pairs[x] for x in y] for y in candidates]:
        group = intersection(*tuple(groups))
        if len(group) == 5:
            length_five.append(group)

    print(sum(min(length_five, key=lambda x: sum(x))))


def intersection(s1, s2, s3, s4):
    return s1.intersection(s2, s3, s4)

def are_compatible(p1, p2):
    s1 = str(p1)
    s2 = str(p2)
    return is_prime(int(s1 + s2)) and is_prime(int(s2 + s1))

def add_item(i1, i2, add_to):
    try:
        add_to[i1].add(i2)
    except KeyError:
        add_to[i1] = {i1, i2}

main()
