def factorize(num_choice):
    factor_list = []
    divisor_list = []
    factor_find(num_choice, factor_list, divisor_list)
    if num_choice not in factor_list:
        for i in divisor_list:
            factor_find(i, factor_list, divisor_list)
        return factor_list
    else:
        return factor_list


def factor_find(dividend, factor_list, divisor_list):
    divisor = 2
    while True:
        if dividend % divisor == 0 and dividend > divisor:
            divisor_list.append(divisor)
            dividend /= divisor
            divisor = 2
        elif dividend == divisor:
            factor_list.append(dividend)
            break
        else:
            divisor += 1

if __name__ == "__main__":
    print(factorize(600851475143))




#This unused function was an attempt to print the prime factors
#in exponential form, but it proved difficult to implement with
#numerical sorting 
#def print_list():
    #for i in factor_list:
        #count_value = factor_list.count(i)
        #final_string = "%d^%d" % (i, count_value)
        #if count_value == 1:
            #final_list.append(str(i))
        #elif final_string not in final_list:
            #final_list.append("%d^%d" % (i, count_value))
        #else:
            #continue
    #factor_list = [round(i) for i in factor_list]
    #print(sorted(final_list))

#https://projecteuler.net/problem=3