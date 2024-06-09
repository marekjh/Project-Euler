total = 0

for number in range(2, 500000):
    digit_sum = 0
    for char in str(number):
        digit_sum += (int(char) ** 5)
    
    if digit_sum == number:
        total += number

print(total)

#https://projecteuler.net/problem=30