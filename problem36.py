def double_palindromes(n):
    total = 0
    
    for number in range(1, n):
        binary_version = bin(number)[2:]
        if str(number) == str(number)[::-1] and binary_version == binary_version[::-1]:
            total += number
    
    return total

print(double_palindromes(1_000_000))
#https://projecteuler.net/problem=36