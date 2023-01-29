def disprove():
    primes = [2, 3]
    num = 5
    while True:    
        if is_prime(num, primes):
            primes.append(num)
        else:
            if not goldbach(num, primes):
                return num
        num += 2
    
def is_prime(n, p):
    i = 0
    while p[i] <= int(n ** 0.5):
        if n % p[i] == 0:
            return False
        i += 1
    return True

def goldbach(n, p):
    for k in p:
        op = ((n - k) / 2) ** 0.5
        if op == int(op):
            return True
    return False

print(disprove())
#https://projecteuler.net/problem=46