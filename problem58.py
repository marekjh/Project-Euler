def spiral_primes(f):
    #primes = [2, 3, 5]
    n = 7
    sidelength = 3
    diagonals = 3 #Numbers 1, 3, and 5
    diag_primes = 2 #Numbers 3 and 5
    while True:
        diagonals += 1
        i = 3
        while i <= int(n ** 0.5):
            if n % i == 0:
                break
            i += 2
        else:
            diag_primes += 1
        if diag_primes / diagonals < f:
            return sidelength
        if n == sidelength ** 2:
            sidelength += 2
        
        n += sidelength - 1
    
print(spiral_primes(0.1))
