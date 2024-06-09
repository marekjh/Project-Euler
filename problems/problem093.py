from itertools import combinations, permutations, product

def main():
    highest = 0
    for c in combinations(range(1, 10), 4):
        seen = set()
        for n1, n2, n3, n4 in permutations(c):
            for s1, s2, s3 in product("+-*/", repeat=3):
                r1 = f"(n1 {s1} n2) {s2} (n3 {s3} n4)"
                r2 = f"(n1 {s1} (n2 {s2} n3)) {s3} n4"
                r3 = f"n1 {s1} ((n2 {s2} n3) {s3} n4)"
                r4 = f"n1 {s1} (n2 {s2} (n3 {s3} n4))"
                r5 = f"((n1 {s1} n2) {s2} n3) {s3} n4"
                for r in (r1, r2, r3, r4, r5):
                    try:
                        r = eval(r)
                    except ZeroDivisionError:
                        pass
                    seen.add(r)
        h = first_unreachable(seen)
        if h > highest:
            highest = h
            combo = c
    print("".join([str(x) for x in combo]))

def first_unreachable(s):
    n = 1
    while n in s:
        n += 1
    return n

main()
    
            