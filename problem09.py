square_numbers_list = []
a_list = []
b_list = []
c_list = []

def add_square_numbers():
    for i in range(1, 999):
        square = i ** 2
        square_numbers_list.append(square)
        
def add_abc():
    for i in square_numbers_list:
        a_squared = i
        for k in square_numbers_list:
            b_squared = k
            if a_squared + b_squared in square_numbers_list and a_squared < b_squared and a_squared not in a_list and b_squared not in b_list:
                a_list.append(a_squared)
                b_list.append(b_squared)
                c_list.append(a_squared + b_squared)
                   
def sum_check():
    i = 0
    while i < len(a_list):
        added_lists = a_list[i] + b_list[i] + c_list[i]  
        multiplied_lists = a_list[i] * b_list[i] * c_list[i]
        if added_lists == 1000:
            break
        else:
            i += 1
    print(multiplied_lists)
        
add_square_numbers()
add_abc()
a_list = [x ** 0.5 for x in a_list]
b_list = [x ** 0.5 for x in b_list]
c_list = [x ** 0.5 for x in c_list]
sum_check()      

#https://projecteuler.net/problem=9