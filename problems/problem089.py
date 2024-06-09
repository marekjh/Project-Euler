R2D = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
D2R = {v:k for k, v in R2D.items()}

def main():
    with open("../data/roman.txt") as f:
        numerals = [x.strip() for x in f.readlines()]
    print(sum(len(x) - len(decimal2roman(roman2decimal(x))) for x in numerals))

def roman2decimal(n):
    total = 0
    i = 0
    while i < len(n):
        curr = R2D[n[i]]
        next = R2D[n[i+1]] if i != len(n)-1 else 0
        diff = next - curr 
        if diff > 0:
            total += diff
            i += 2
        else:
            total += curr
            i += 1
    return total

def decimal2roman(n):
    numeral = ""
    for p in (1000, 100, 10, 1):
        d = n//p
        if p != 1000 and d in (4, 9):
            numeral += D2R[p] + D2R[(d+1)*p]
        else:
            if d >= 5:
                numeral += D2R[5*p]
                d -= 5
            numeral += d * D2R[p]
        n %= p
    return numeral

main()