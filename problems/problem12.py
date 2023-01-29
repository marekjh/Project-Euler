factor_count = 0
triangle_num = 0
counter = 0
divisor = 1


while True:
    counter += 1
    triangle_num += counter
    while factor_count <= 500:
        check = 0
        if divisor <= triangle_num ** 0.5:
            modulus = triangle_num % divisor
            division = triangle_num / divisor
            if modulus == 0 and division == divisor:
                factor_count += 1
                divisor += 1
            elif modulus == 0:
                factor_count += 2
                divisor += 1
            else:
                divisor += 1
        else:
            check = 1
            divisor = 1
            factor_count = 0
            break
    if check == 0:
        break
         
print(triangle_num)
        
#https://projecteuler.net/problem=12