from primes import SORTED_PRIMES as p

N = 50
squares = [x**2 for x in p[p < N**(1/2)]]
cubes = [x**3 for x in p[p < N**(1/3)]]
fourths = [x**4 for x in p[p < N**(1/4)]]

nums = set()
for x in squares:
    for y in cubes:
        for z in fourths:
            nums.add(x + y + z)
print(len(nums))