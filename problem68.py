from itertools import permutations

def main():
    solutions = set()
    for p in permutations(range(1, 10), 5):
        (x5, x6, x7, x8, x9) = p
        x1 = x5 + x6 - x7 + x8 - 10
        x2 = x5 + x9 - 10
        x3 = x5 - x7 + x8
        x4 = x5 + x6 - x7 + x9 - 10
        sol = (x1, x2, x3, x4) + p
        if len(set(sol)) == 9 and all(x in range(1, 10) for x in sol):
            solutions.add(sol)
    print(max(get_string(sol) for sol in solutions))
        

def get_string(vals):
    vals = [str(v) for v in vals]
    (x1, x2, x3, x4, x5, x6, x7, x8, x9) = vals
    sums = [x6 + x2 + x3, x7 + x3 + x4, x8 + x4 + x5, x9 + x5 + x1, "10" + x1 + x2]
    start_position = vals.index(min(vals[5:])) - 5
    out = ""
    for s in sums[start_position:] + sums[:start_position]:
        out += s
    return out

main()