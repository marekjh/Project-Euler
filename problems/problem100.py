def main():
    N = 10**12
    x, y = 2*120 - 1, 2*85 - 1  # Starting solution has 120 total discs, 85 blue discs

    while (x+1)//2 <= N:
        x, y = step(x, y)
    print((y+1)//2)

# Used info at https://math.stackexchange.com/questions/531833/generating-all-solutions-for-a-negative-pell-equation
def step(x, y):
    x_next = 3*x + 4*y
    y_next = 2*x + 3*y
    return x_next, y_next

main()