def main():
    N = 10**9
    x_plus, y_plus = 5, 8
    x_minus, y_minus = 17, 30
    total = 0
    while max(x_plus, x_minus) < N/3:
        total += 3*(x_plus + x_minus)
        x_plus, y_plus = step(x_plus, y_plus, 1)
        x_minus, y_minus = step(x_minus, y_minus, -1)
    print(total)

def step(x, y, sign):
    x_next = 7*x + 4*y - 2*sign
    y_next = 12*x + 7*y - 4*sign
    return x_next, y_next

main()