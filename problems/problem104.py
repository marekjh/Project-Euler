from math import log10, sqrt

def main():
    N = 9
    phi = (1+sqrt(5))/2
    prev, curr = 1, 1
    k = 2
    while True:
        if pandigital(curr):
            exp = k*log10(phi/sqrt(5)**(1/k))       # Log of large k approximation of fibonacci numbers
            first = int(10**(exp-int(exp)+N-1))     # First 9 digits of kth fibonacci number 
            if pandigital(first):
                print(k)
                return              
        prev, curr = curr, (prev+curr) % 10**N
        k += 1

def pandigital(x):
    return set(str(x)) == set("123456789")

main()

# Thanks to Philip Nilsson from the problem 104 thread for the math in this elegant solution!