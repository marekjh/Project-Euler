def x_digit_fib_number(x):
    a = 1
    b = 1
    count = 2
    
    while True:        
        c = a + b
        count += 1
        
        if len(str(c)) == x:
            return count
        
        a = b + c
        count += 1
        
        if len(str(a)) == x:
            return count
        
        b = c + a
        count += 1
        
        if len(str(b)) == x:
            return count

print(x_digit_fib_number(1000))
#https://projecteuler.net/problem=25