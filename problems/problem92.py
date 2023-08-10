N = 10_000_000

seen_yes = set()
seen_no = set()
for n in range(2, N):
    next = n
    while next != 89 and next not in seen_yes:
        next = sum(int(x)**2 for x in str(next))
        if next == 1 or next in seen_no:
            seen_no.add(n)
            break
    else:
        seen_yes.add(n)
print(len(seen_yes))

