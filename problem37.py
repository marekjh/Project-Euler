prime_list = [2, 3]

def find_truncated_primes():
    count = 0
    total = 0
    number = 5
    
    while count < 11:
        if is_prime(number):
            prime_list.append(number)
            if is_truncated(number):
                count += 1
                total += number
        number += 2
    return total

def is_prime(num):
    if num < 2:
        return False
    i = 0
    while prime_list[i] <= num ** 0.5:
        if num % prime_list[i] == 0:
            return False
        i += 1
    return True

def is_truncated(num):
    if num < 10:
        return False
    num = str(num)
    for i in range(1, len(num)): 
        if not (is_prime(int(num[i:])) and is_prime(int(num[:i]))):
            return False
    return True

print(find_truncated_primes())


            
            
#https://projecteuler.net/problem=37