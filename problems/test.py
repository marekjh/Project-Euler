def sum_of_divisors(n):
    # Calculate the sum of proper divisors of n
    divisors_sum = 1  # Start with 1 as every number is divisible by 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def find_amicable_chain_length(start, limit):
    chain = []
    current = start

    while current < limit:
        if current in chain:
            # We've found a cycle, so break the loop
            break

        chain.append(current)
        next_number = sum_of_divisors(current)

        if next_number == current:
            # The number is part of an amicable pair with itself
            chain.append(current)
            break

        current = next_number

    return len(chain)

def find_longest_amicable_chain(limit):
    max_length = 0
    max_start = 0

    for start in range(2, limit):
        if start % 2 == 0:  # Skip even numbers for efficiency
            continue

        chain_length = find_amicable_chain_length(start, limit)

        if chain_length > max_length:
            max_length = chain_length
            max_start = start

    return max_start, max_length

limit = 1000000
start, length = find_longest_amicable_chain(limit)
print(f"The longest amicable chain starts with {start} and has length {length}.")