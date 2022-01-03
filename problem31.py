def coin_sum(amount):
    total = 1 #starts with the 2-pound coin accounted for
    denominations = {100:0, 50:0, 20:0, 10:0, 5:0}
    
    while True:
        check = 0
        for denom in denominations:
            check += denom * denominations[denom]
        if check <= amount:
            total += (amount - check) // 2 + 1
            
        for denom in sorted(denominations.keys()):
            if denominations[denom] == amount / denom:
                denominations[denom] = 0
            else:
                denominations[denom] += 1
                break
        else:
            return total

print(coin_sum(200))
#https://projecteuler.net/problem=31