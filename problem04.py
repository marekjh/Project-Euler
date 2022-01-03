pal_list = []

def find_pal():
    a = 100
    while a in range(100, 1000):
        for b in range(100, 1000):
            product = a * b
            if str(product) == str(product)[::-1]:
                pal_list.append(product)
            else:
                continue
        a += 1
    print(max(pal_list))

find_pal()


#https://projecteuler.net/problem=4