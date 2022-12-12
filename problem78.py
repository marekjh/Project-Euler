# Uses MacMahon Recurrence
def find_partition(N):
    partition = 1
    partitions = [1]
    ub = 500
    pent = [int(x*(3*x - 1)/2) for x in range(1, ub)]
    pent.extend([int(x*(3*x + 1)/2) for x in range(1, ub)])
    pent.sort()

    n = 0
    while partition % N != 0:
        partition = 0
        for i, p in enumerate(pent):
            if p > len(partitions):
                break
            prev = partitions[-p]
            if i % 4 in (2, 3):
                prev *= -1
            partition += prev
        partitions.append(partition)
        n += 1
    return n
            
print(find_partition(1_000_000))
