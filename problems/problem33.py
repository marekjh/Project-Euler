def calc_denominator():    
    num_product = 1
    den_product = 1
    
    for denominator in range(11, 100): 
        for numerator in range(11, denominator): 
            den_string = str(denominator)
            num_string = str(numerator)
            
            for digit in num_string:
                if digit in den_string and digit != "0":
                    num_string = num_string.replace(digit, "", 1)
                    den_string = den_string.replace(digit, "", 1)
                    
                    try:
                        if numerator / denominator == int(num_string) / int(den_string):
                            num_product *= numerator
                            den_product *= denominator
                    #This block takes care of palindromic numerator/denominator pairs and cases where 0 is left in denominator
                    except (ZeroDivisionError, ValueError): 
                        pass
    
    while True: #Reduces the fraction num_product/den_product
        for num in range(num_product // 2 + 1, 1, -1):
            if num_product % num == 0 and den_product % num == 0:
                num_product //= num
                den_product //= num
                break
        else:
            return den_product
        
print(calc_denominator())

#https://projecteuler.net/problem=33