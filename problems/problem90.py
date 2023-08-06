from itertools import combinations

def main():
    cubes = [set(x) for x in combinations(range(10), 6)]
    for c in cubes:
        if 6 in c:
            c.add(9)
        elif 9 in c:
            c.add(6)
    pairs = combinations(cubes, 2)

    total = 0
    for pair in pairs:
        if all_squares(pair):
            total += 1
    print(total)

def all_squares(pair):
    squares = {"01", "04", "09", "16", "25", "36", "49", "64", "81"}
    c1, c2 = pair
    for s in squares:
        s1, s2 = int(s[0]), int(s[1])
        if not (s1 in c1 and s2 in c2 or s1 in c2 and s2 in c1):
            return False
    return True

main()


