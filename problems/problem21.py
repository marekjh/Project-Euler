def amicable_numbers(n):
    div_sum_dict = {}
    amicable_total = 0

    for number in range(4, n):
        divisor_sum_total = 1
        
        for check_number in range(2, int(number ** 0.5) + 1):
            if number % check_number == 0:
                divisor = number // check_number
                divisor_sum = divisor + check_number
                
                if divisor == check_number:
                    divisor_sum -= divisor
                
                divisor_sum_total += divisor_sum
        
        if number != divisor_sum_total:
            div_sum_dict[number] = divisor_sum_total
            
            if divisor_sum_total <= max(div_sum_dict.keys()):
                if (number, divisor_sum_total)[::-1] in div_sum_dict.items():
                    amicable_total += (number + divisor_sum_total)

    return amicable_total

try:
    n_choice = int(input("Choose a cap under which to sum amicable numbers: "))
except ValueError:
    print("Selected value must be an integer")
else:
    print(f"{amicable_numbers(n_choice)}")
#https://projecteuler.net/problem=21