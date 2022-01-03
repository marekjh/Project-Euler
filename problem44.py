def build(start, nums):
    for n in range(start, start * 2):
        nums.append(n * (3 * n - 1) / 2)
    return nums

def find_difference():
    pentagons = [1]
    while True:
        for i in pentagons:
            for j in pentagons:
                while pentagons[-1] < i + j:
                    pentagons = build(len(pentagons) + 1, pentagons)
                if j == i:
                    break
                if i - j in pentagons and i + j in pentagons:
                    return i - j

print(find_difference())
#https://projecteuler.net/problem=44