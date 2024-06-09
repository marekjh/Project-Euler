from math import ceil

def main():
    N = 1_000_000
    sols = 0
    m = 0
    while sols < N:
        m += 1
        bases = [(i, m) for i in range(1, 2*m+1)]
        for b1, b2 in bases:
            if pythagorean(b1, b2):
                sols += num_cuboids(b1, b2)
        
    print(m)

def pythagorean(x, y):
    z = (x**2 + y**2)**(1/2)
    return z == int(z)

def num_cuboids(a, b):
    if a > 2*b:
        return 0
    n = a - 1
    if a >= b + 2:
        n -= 2*(a - b - 1)
    return ceil(n/2)

if __name__ == "__main__":
    main()