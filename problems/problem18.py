def triangle_constructor(input_file):
    f = open(input_file, "r")
    triangle_list = []
    
    for line in f:
        line = line.strip()
        row = line.split()
        row = [int(x) for x in row]
        triangle_list.append(row)
    f.close()
    
    return triangle_list

def extreme_sum(triangle, f):
    if len(triangle) == 1:
        return triangle[0][0]

    check_row = triangle[-1]
    current_row = triangle[-2]
    replacement_row = []
    
    for i in range(len(current_row)):
        left_path = check_row[i]
        right_path = check_row[i + 1]
        best_path = current_row[i] + f([left_path, right_path])
        replacement_row.append(best_path)
    
    del triangle[-1]
    triangle[-1] = replacement_row
    
    return extreme_sum(triangle, f)
            
if __name__ == "__main__":
    input_triangle = triangle_constructor("../data/nums_in_triangle2.txt")
    print(extreme_sum(input_triangle, max))

#https://projecteuler.net/problem=18