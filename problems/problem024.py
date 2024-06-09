import math

def permute_nums(input_string, term):
    term -= 1
    
    running_list = list(input_string)
    num_digits = len(running_list)
    
    output_string = ""
    
    for i in range(num_digits, 0, -1):
        permutations = math.factorial(i - 1)
        quotient = term // permutations
        output_string += str(running_list[quotient])
        del running_list[quotient]
        term -= (permutations * quotient)
    
    return output_string

if __name__ == "__main__":
    try:
        digits = input("Enter a string of digits to permute (no spaces/punctuation): ")
        looking_for = int(input("Check the nth item in the lexicographically sorted list of permutations where n = "))
        
        test = int(digits)
    except (TypeError, ValueError):
        print("\nFollow input instructions")
    else:
        try:
            if looking_for < 1:
                test2 = int(" ")
            print("\n" + permute_nums(digits, looking_for))
        except (ValueError, IndexError):
            print("\n" + f"n must be in the range [1, {len(digits)}!]")
    
        
        
        
    

#https://projecteuler.net/problem=24