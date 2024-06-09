from problem24 import permute_nums
from math import factorial

def pandigital_sum():
    total = 0
    for num in range(factorial(9) + 1, factorial(10) + 1):
        pandigital = permute_nums("0123456789", num)
        if sub_string_check(pandigital):
            total += int(pandigital)
    
    return total

def sub_string_check(n):
    prime_list = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, len(str(n)) - 2):
        sub_string = n[i:i + 3]
        if int(sub_string) % prime_list[i - 1] != 0:
            return False
    return True

print(pandigital_sum())
        
#https://projecteuler.net/problem=43