import math
total = 0

for number in range(3, 50000):
    count = 0
    for digit in str(number):
        count += math.factorial(int(digit))
    
    if count == number:
        total += number

print(total)
#https://projecteuler.net/problem=34