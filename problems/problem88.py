from math import prod
from collections import Counter
from numpy import inf

M = 12_000

def main():
    nums = ProductSumNums(M)
    min_product_sums = {}
    try:
        while True:
            nums.increment()
            n = nums.size()
            p = nums.product()
            if n > 1 and p < min_product_sums.get(n, inf):
                min_product_sums[n] = p
    except Exception:
        print(sum(set(min_product_sums.values())))

class ProductSumNums:
    def __init__(self, M):
        self.M = M
        self.nums = Counter()
    
    def increment(self):
        self.nums += Counter({2:1})
        x = 2**self.nums[2]
        n = 2
        while self.size() > self.M:
            del self.nums[n]
            if n+1 > x:
                n = min(self.nums) + 1 if len(self.nums) > 0 else n+1
                del self.nums[n-1]
            else:
                n += 1
            if n > self.M:
                raise Exception("Cannot be incremented further")
            self.nums += Counter({n:1})
            lowest = min(self.nums)
            x = lowest**self.nums[lowest]
            
    def size(self):
        return self.product() - self.sum() + sum(self.nums.values())

    def product(self):
        return prod([x**self.nums[x] for x in self.nums])

    def sum(self):
        return sum([x*self.nums[x] for x in self.nums])


main()