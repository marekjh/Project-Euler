count = 0
for p in range(1, 22):
    for x in range(1, 10):
        if len(str(x ** p)) == p:
            count += 1
print(count)