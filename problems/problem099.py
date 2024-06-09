from math import log

def main():
    largest = 0
    for i, (base, exp) in enumerate(read_file("../data/0099_base_exp.txt")):
        x = log(base)*exp
        if x > largest:
            largest = x
            largest_i = i
    print(largest_i+1)

def read_file(file):
    with open(file) as f:
        return [tuple([int(x) for x in y.strip().split(",")]) for y in f.readlines()]
    
main()