def even_fib_numbers(max_num):
    a = 1
    b = 1
    even_total = 0    
    
    while b < max_num:
        if b % 2 == 0:
            even_total += b
        c = a + b
        a = b
        b = c
    
    return even_total
num_choice = int(input("Choose a value, and the program will sum the even Fibonacci numbers less than that value: "))
print("\n%d" % even_fib_numbers(num_choice))

#https://projecteuler.net/problem=2