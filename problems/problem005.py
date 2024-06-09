x = 2520

while True:
    for i in range(2, 20):
        divis_check = x % i
        if divis_check != 0:
            a = 0
            break
        elif divis_check == 0 and i == 19:
            a = 1
            break
        else:
            continue
    if a == 0:
        x += 20
    else:
        break

print(x)
            
        

#https://projecteuler.net/problem=5