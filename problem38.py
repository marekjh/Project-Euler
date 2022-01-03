def pandigital_find(n):
    for num in range(int("9" * (n // 2)), 0 , -1):
        cat_string = str(num)
        multiplier = 2
        while len(cat_string) < n:
            cat_string += str(num * multiplier)
            multiplier += 1
        if set(cat_string) == {str(x) for x in range(1, n + 1)} and len(cat_string) == n:
            return cat_string

print(pandigital_find(9))
        
    
    
            
        
        
        
    
    
    
#https://projecteuler.net/problem=38