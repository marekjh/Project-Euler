max_num = int(input("Select a number, and the program will print the sum of primes less than that number: "))

prime_list = [2, 3]

def prime_sum(n):
    dividend = 5
    while dividend < n:  
        for i in prime_list:
            if i > dividend ** 0.5:
                prime_list.append(dividend)
                dividend += 2
                break
            elif dividend % i == 0:
                dividend += 2
                break
            else:
                continue
    print(sum(prime_list))

prime_sum(max_num)
#https://projecteuler.net/problem=10