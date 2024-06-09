def main():
    P = (0, 0)
    triangles = read_file("../data/0102_triangles.txt")
    
    total = 0
    for triangle in triangles:
        if contains_point(triangle, P):
            total += 1
    print(total)
    
def contains_point(triangle, point):
    a, b, c = triangle
    for u, v, w in (a, b, c), (b, c, a), (c, a, b):
        if not half_plane(point, u, v, w):
            return False
    return True

def half_plane(p, x, y, z):
    '''Returns true if and only if point p lies in the half plane defined by the 
    line passing through points x, y and containing the triangle x, y, z'''

    p1, p2 = p; x1, x2 = x; y1, y2 = y; z1, z2 = z

    if x1 == y1: # Handle vertical line case to avoid division by zero
        compare = ">" if z1 > x1 else "<="
        rhs = "x1"
    else:
        m = (y2-x2)/(y1-x1)
        compare = ">" if z2-x2 > m*(z1-x1) else "<="
        rhs = "m*(p1-x1)"
    return eval(f"p2-x2 {compare} {rhs}")

def read_file(file):
    with open(file) as f:
        lines = [[int(y) for y in x.strip().split(",")] for x in f.readlines()]
    return [(tuple(x[:2]), tuple(x[2:4]), tuple(x[4:6])) for x in lines]
    
main()