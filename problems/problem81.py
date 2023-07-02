from problem18 import extreme_sum

def triangle_constructor(file):
    with open(file) as f:
        M = [[int(x) for x in y.split(",")] for y in f.readlines()]
    triangle = []
    for i in range(len(M)):
        row = []
        for j in range(i+1):
            row.append(M[i-j][j])
        triangle.append(row)
    c = 10_000
    for i in range(1, len(M)):
        row = []
        for j in range(len(M)-i):
            row.append(M[-j-1][i+j])
        for _ in range(i):
            row.insert(0, c)
            row.append(c)
        triangle.append(row)
    return triangle

triangle = triangle_constructor("../data/matrix.txt")
print(extreme_sum(triangle, min))

