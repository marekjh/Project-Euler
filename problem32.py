def identity_find():
    total = 0
    
    for num in range(1000, 10_000): #All four digit numbers
        digit_list = []    
    
        for char in str(num):
            if char in digit_list:
                break
            digit_list.append(char)
        else:
            for divisor in range(2, int(num ** 0.5) + 1):
                if num % divisor == 0:
                    for char in str(divisor):
                        digit_list.append(char)
                    for char in str(num // divisor):
                        digit_list.append(char)
                    
                    if sorted(digit_list) == [str(x) for x in range(1, 10)]:
                        print((num, divisor, num // divisor))
                        total += num
                        break
                    del digit_list[4:] #Delete all items except the digits of the product num

    return total

print(identity_find())
#https://projecteuler.net/problem=32