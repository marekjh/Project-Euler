max_num = int(input("Find the starting number of a Collatz sequence that has the greatest number of terms of all sequences with starting numbers <= n where n = "))


def collatz_check(n):
    starter_list = []
    counter_list = []
    counter = 0    
    for i in range(1, n + 1):    
        starter_list.append(i)
        term = i
        while term > 1:
            if term % 2 == 0:
                term /= 2
                counter += 1
            else:
                term = term * 3 + 1
                counter += 1
        counter += 1
        counter_list.append(counter)
        counter = 0
    print("\nStarting number: %d" % starter_list[counter_list.index(max(counter_list))])
    print("Number of terms: %d" % max(counter_list))

collatz_check(max_num)
#https://projecteuler.net/problem=14