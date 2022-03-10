from problem03 import factorize

def find_consecutive():
    count = 0
    num = 5
    while True:
        if len(set(factorize(num))) == 4:
            count += 1
        else:
            count = 0
        if count == 4:
            return num - 3
        num += 1

print(find_consecutive())
#https://projecteuler.net/problem=47