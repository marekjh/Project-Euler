def square_of_sum():
    a = 0
    for i in range(101):
        a += i
    return a ** 2

def sum_of_squares():
    squares_list = []
    for i in range(101):
        b = i ** 2
        squares_list.append(b)
    return sum(squares_list)
    
print(square_of_sum() - sum_of_squares())
#https://projecteuler.net/problem=6