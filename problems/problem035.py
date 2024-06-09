#will create a list of primes below 1010 (~1_000_000 ** 0.5) to use in is_prime
def create_prime_list():
    primes = [2, 3]
    for num in range(5, 1010, 2):
        i = 0
        while primes[i] <= num ** 0.5:
            if num % primes[i] == 0:
                break
            i += 1
        else:
            primes.append(num)
    
    return primes

def is_circular(number):
    digits = str(number)
    for _ in range(len(digits) - 1):
        check = f"{digits[-1]}"
        for digit in digits[:-1]:
            check += digit
        
        if not is_prime(int(check), prime_list):
            return False
        digits = check    
    
    return True

def is_prime(number, primes):
    i = 0
    while primes[i] <= number ** 0.5:
        if number % primes[i] == 0:
            return False
        i += 1
    return True   

total = 2 #2 and 3 already included
prime_list = create_prime_list()

for num in range(5, 1_000_000, 2):
    if is_prime(num, prime_list):
        if is_circular(num):
            total += 1
print(total)
#https://projecteuler.net/problem=35