multiple_list = []

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        multiple_list.append(i)
        
print(sum(multiple_list))

#https://projecteuler.net/problem=1
        
