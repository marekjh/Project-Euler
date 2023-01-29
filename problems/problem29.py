def distinct_powers():
    powers_list = []
    
    for a in range(2, 101):
        for b in range(2, 101):
            power = b ** a
            if power not in powers_list:
                powers_list.append(power)
    
    return len(powers_list)

print(distinct_powers())
#https://projecteuler.net/problem=29