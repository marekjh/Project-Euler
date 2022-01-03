import math

def path_count(length, width):
    combination = math.factorial(length + width) / (math.factorial(length) * math.factorial(width))
    return int(combination)

side_1 = int(input("Choose the first sidelength of a grid: "))
side_2 = int(input("Choose the second sidelength of a grid: "))

num_paths = path_count(side_1, side_2)
print("\nThe number of paths from top left to bottom right, using only movements right or down, is %d" % num_paths )
        
        
        
    
    
    
    
    
#https://projecteuler.net/problem=15