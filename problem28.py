def sum_spiral(dimension):
    total = 1
    num = 1
    sidelength = 0
    jump = 2
    
    while sidelength < dimension:
        sidelength = jump + 1
        square_num = sidelength ** 2
        
        while num < square_num:
            num += jump
            total += num

        jump += 2
    
    return total 

print(sum_spiral(1001))
#https://projecteuler.net/problem=28