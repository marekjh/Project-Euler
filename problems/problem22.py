def prepare_list(input_file):
    f = open(input_file, "r")
    contents = f.read()
    contents = contents.replace('"', "")
    contents_list = contents.split(",")
    contents_list.sort()
    
    letter_val_dict = {}
    count = 1
    for i in range(65, 91):
        letter_val_dict[chr(i)] = count
        count += 1
    
    return (contents_list, letter_val_dict)

def calculate_score(info_tuple):
    (name_list, val_dict) = info_tuple
    score = 0
    
    for i in range(len(name_list)):
        name_total = 0
        
        for char in name_list[i]:
            name_total += val_dict[char]
        
        score += ((i + 1) * name_total)
    
    return score

list_and_dict = prepare_list("names_list.txt")
print(calculate_score(list_and_dict))
#https://projecteuler.net/problem=22