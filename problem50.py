def generate_primes(n_max):
    primes = [2, 3]
    for n in range(5, n_max // 100, 2):
        i = 0
        while primes[i] <= int(n ** 0.5):
            if n % primes[i] == 0:
                break
            i += 1
        else:
            primes.append(n)
    return primes

def is_prime(n, p):
    i = 0
    while p[i] <= int(n ** 0.5):
        if n % p[i] == 0:
            return False
        i += 1
    return True

def prime_sum(N):
   primes = generate_primes(N)
   K = 1 
   for i in range(len(primes) - 1, 0, -1):
      for k in range(K):
         prime_sum = sum(primes[k:i + k]) 
         if prime_sum < N and is_prime(prime_sum, primes):
            return prime_sum
      K += 1

print(prime_sum(1000000))
#https://projecteuler.net/problem=50