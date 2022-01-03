def crazy_num_function():
    big_str = str(2 ** 1000)
    big_list = list(big_str)
    int_list = [int(x) for x in big_list]
    final_sum = sum(int_list)
    return final_sum
    
print(crazy_num_function())
#https://projecteuler.net/problem=16