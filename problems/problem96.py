def main():
    puzzles = read_file("../data/p096_sudoku.txt")
    total = 0
    for puzzle in puzzles:
        sol = solve(puzzle)
        # total += sum(sol[0][:3])


def solve(puzzle):
    moves_needed = sum(row.count(0) for row in puzzle)
    for _ in range(moves_needed):
        pass
    
def update_candidates(puzzle, i, j):
    pass
def read_file(file):
    out = []
    with open(file, "r") as f:
        lines = [x.strip() for x in f.readlines()]
    for n in range(1, len(lines)//10 + 1):
        lines.remove(f"Grid {'0' + str(n) if n < 10 else n}")
    lines = [[int(x) for x in list(y)] for y in lines]
    for i in range(0, len(lines), 9):
        out.append(lines[i:i+9])
    return out
        

main()

