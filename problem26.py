def cycles(N):
    nums = [n for n in range(11, N) if n % 2 != 0 and n % 5 != 0]
    k = 1
    while len(nums) > 1:
        for num in nums:
            nines = 10 ** k - 1
            if nines % num == 0:
                nums.remove(num)
        k += 1
    return nums[0]


print(cycles(1000))
#https://projecteuler.net/problem=26