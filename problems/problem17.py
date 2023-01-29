def letter_count():
    counting_string = ""
    naming_list_1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    naming_list_2 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    for i in range(1, 1001):
        first_digit = int(str(i)[0])
        if i == 1000:
            counting_string += "onethousand"
        elif i < 20:
            counting_string += naming_list_1[i - 1]
        elif i < 100:
            second_digit = int(str(i)[1])
            if second_digit == 0:
                counting_string += naming_list_2[first_digit - 2] 
            else:
                counting_string += naming_list_2[first_digit - 2] + naming_list_1[second_digit - 1]
        else:
            second_digit = int(str(i)[1])
            third_digit = int(str(i)[2])
            last_two_digits = int(str(i)[1:])
            if last_two_digits == 0:
                counting_string += naming_list_1[first_digit - 1] + "hundred"
            elif last_two_digits < 20:
                counting_string += naming_list_1[first_digit - 1] + "hundredand" + naming_list_1[last_two_digits - 1]
            elif third_digit == 0:
                counting_string += naming_list_1[first_digit - 1] + "hundredand" + naming_list_2[second_digit - 2]
            else:
                counting_string += naming_list_1[first_digit - 1] + "hundredand" + naming_list_2[second_digit - 2] + naming_list_1[third_digit - 1]
    
    return len(counting_string)

print(letter_count())
#https://projecteuler.net/problem=17