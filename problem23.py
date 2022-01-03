def abundant_check(num):
    factor_sum = 1
        
    for num_check in range(2, int((num ** 0.5) + 1)):
        if num % num_check == 0:
            factor = num // num_check
            factor_sum += (factor + num_check)
            
            if factor == num_check:
                factor_sum -= factor
    
    return factor_sum > num

def non_abundant_sum(abundant_list):
    final_total = 0
    
    for number in range(1, 28_123):
        check = True
        
        for abundant_num in abundant_list:
            if abundant_num >= number:
                break
            diff = number - abundant_num
            if abundant_check(diff):
                check = False
                break
        
        if check:
            final_total += number
    
    return final_total
        
abundant_num_list = []

for number in range(12, 14_062): #Upper bound is half of the bound for the sum of two abundant numbers        
    if abundant_check(number):
        abundant_num_list.append(number)

print(non_abundant_sum(abundant_num_list))

#https://projecteuler.net/problem=23