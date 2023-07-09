import numpy as np

def main():
    N = 2_000_000
    m = 1
    low = np.inf
    while True:
        n = root(m*(m+1)/4, m*(m+1)/4, -N)
        if n < m:
            break
        n = int(n)
        diff = abs(R(n, m) - N)
        if diff < low:
            low = diff
            area = m*n
        m += 1
    print(area)

# Found utilizing recurrence relation
# Also (more easily seen) product of triangular numbers
def R(m, n):
    return m*(m+1)*n*(n+1)/4

def root(a, b, c):
    return (-b + (b**2 - 4*a*c)**(1/2))/(2*a)

main()