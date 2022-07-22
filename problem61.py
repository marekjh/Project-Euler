from itertools import permutations
from copy import deepcopy

def main():
    polygonals = [set() for _ in range(6)]
    functions = [triangle, square, pentagon, hexagon, heptagon, octagon]

    for i, f in enumerate(functions):
        n = 1
        while True:
            fn = f(n)
            if fn >= 1000 and fn < 10000:
                polygonals[i].add(fn)
            elif fn >= 10000:
                break
            n += 1

    print(find_cycle(polygonals))

def find_cycle(arr):
    copy = deepcopy(arr)
    for ordering in permutations(range(6), 6):
        for _ in range(2):
            for i in range(len(ordering) - 1):
                reduce(ordering[i], ordering[i + 1], copy)
            reduce(ordering[-1], ordering[0], copy)
            if all(len(x) == 1 for x in copy):
                return sum(tuple(x)[0] for x in copy)
        copy = deepcopy(arr)

def reduce(i, j, arr):
    candidates = []
    for n1 in arr[i]:
        for n2 in arr[j]:
            if str(n1)[-2:] == str(n2)[:2]:
                candidates.append((n1, n2))
    arr[i] = {x[0] for x in candidates}
    arr[j] = {x[1] for x in candidates}

def triangle(n):
    return n * (n + 1) // 2

def square(n):
    return n ** 2

def pentagon(n):
    return n * (3 * n - 1) // 2

def hexagon(n):
    return n * (2 * n - 1)

def heptagon(n):
    return n * (5 * n - 3) // 2

def octagon(n):
    return n * (3 * n - 2)

main()