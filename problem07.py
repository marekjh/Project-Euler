term_choice = int(input("Find out the nth prime number. n = "))

prime_list = [2, 3]

def check_prime(n):
    dividend = 5
    p = 2
    if n == 1:
        print(2)
    else:
        while p < n:  
            for i in prime_list:
                if i > dividend ** 0.5:
                    prime_list.append(dividend)
                    dividend += 2
                    p += 1
                    break
                elif dividend % i == 0:
                    dividend += 2
                    break
                else:
                    continue
        print(max(prime_list))

check_prime(term_choice)
#https://projecteuler.net/problem=7