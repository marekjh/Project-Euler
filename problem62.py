def find_cube():
    n = 1
    tracker = {}
    while True:
        cube = n ** 3
        pattern = str(sorted(str(cube)))
        try:
            tracker[pattern][0] += 1
        except KeyError:
            tracker[pattern] = [1, cube]
        if tracker[pattern][0] == 5:
            return tracker[pattern][1]
        n += 1
        

print(find_cube())