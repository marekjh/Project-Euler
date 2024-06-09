import numpy as np

def main():
    u_n = input("Enter the coefficients of the polynomial in n for the nth term of the sequence using space-separated values: ")
    u_n = [int(x) for x in u_n.split()]

    total = 0
    for k in range(1, len(u_n)+1):
        possible_fit = op(k, k+1, u_n)
        if possible_fit != evaluate(u_n, k+1):
            total += possible_fit
    print(int(total))
    
def op(k, n, u):
    A = np.array([[y**x for x in range(k)] for y in range(1, k+1)])
    b = np.array([evaluate(u, x) for x in range(1, k+1)])
    return evaluate(np.linalg.solve(A, b).round().astype(int), n)

def evaluate(p, x):
    return np.polynomial.polynomial.polyval(x, p)

main()