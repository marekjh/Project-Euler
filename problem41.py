from problem24 import permute_nums
from math import factorial

def pandigital_prime():
    for i in range(9, 0, -2):
        digit_string = "".join([str(x) for x in range(1, i + 1)])
        for j in range(factorial(i), 0, -1):
            num = int(permute_nums(digit_string, j))
            if is_prime(num):
                return num
        
def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(pandigital_prime())
#https://projecteuler.net/problem=41