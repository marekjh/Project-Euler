N = 9  # Should be a square number

def main():
    puzzles = read_file("../data/p096_sudoku.txt")
    total = 0
    for puzzle in puzzles:
        sol = solve(set_puzzle(puzzle))
        total += int("".join(sol[0][:3]))
    print(total)


def solve(puzzle):
    remaining = set()
    for i in range(N):
        remaining = remaining.union({(i, j) for j in range(N)})
    grid = split_grid()
    while len(remaining) > 0:
        for move in (naked_single, hidden_single, locked_candidates):
            deduction_made = move(puzzle, remaining, grid)
            if deduction_made is None:
                return None
            if deduction_made:
                break
        else:
            for space in remaining:
                i, j = space
                for n in puzzle[i][j]:
                    puzzle[i][j] = {n}
                    sol = solve(puzzle)
                    if sol is not None:
                        return sol
                return None
    return puzzle

    
def update_candidates(puzzle, remove, i, j):
    removed = puzzle[i][j].intersection(remove)
    puzzle[i][j] -= remove
    if len(puzzle[i][j] == 0):
        return None
    return len(removed) > 0

def naked_single(puzzle, spaces, grid):
    pass

def hidden_single(puzzle, spaces, grid):
    pass

def locked_candidates(puzzle, spaces, grid):
    pass

def set_puzzle(puzzle):
    for i in range(len(puzzle)):
        for j, e in enumerate(puzzle[i]):
            if e:
                puzzle[i][j] = {e}
            else:
                puzzle[i][j] = {x for x in range(N)}
    return puzzle

def split_grid():
    rows = [{(i, j) for j in range(N)} for i in range(N)]
    cols = [{(i, j) for i in range(N)} for j in range(N)]
    blocks = []; n = int(N**0.5)
    for i in range(n):
        row = []
        for j in range(n):
            spaces = set()
            for k in range(n):
                spaces = spaces.union({(i*n + k, j*n + l) for l in range(n)})
            row.append(spaces)
        blocks.append(row)
    return {"rows": rows, "cols": cols, "blocks": blocks}

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
 
if __name__ == "__main__":  
    puzzles = read_file("../data/p096_sudoku.txt")
    puzzle = set_puzzle(puzzles[0])
    print(puzzle[0])
    print(update_candidates(puzzle, {4, 5, 6}, 0, 2))
    print(puzzle[0])

