def find_constant():
    fractional_string = ""
    num = 1
    while len(fractional_string) < 1_000_000:
        fractional_string += str(num)
        num += 1
    final_product = 1
    for power in range(7):
        final_product *= int(fractional_string[10 ** power - 1])
    return final_product

print(find_constant())
#https://projecteuler.net/problem=40