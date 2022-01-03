f = open("large_num_text.txt", "r")
string_list = []
for line in f:
    line = line.strip()
    string_list.append(line)

int_list = [int(y) for y in string_list]
final_num = str(sum(int_list))
print(final_num[:10])
#https://projecteuler.net/problem=13