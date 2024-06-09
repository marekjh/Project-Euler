def main():
    f = open("triangle_words.txt", "r")
    contents = f.read()
    contents = contents.replace('"', '')
    word_list = contents.split(",")
    max_len = max(len(x) for x in word_list)
    print(word_count(word_list, max_len))

def word_count(words, x):
    count = 0
    
    triangle_nums = {}
    n = 1
    triangle = 0
    while triangle < 26 * x:
        triangle = 0.5 * n * (n + 1)
        triangle_nums[triangle] = n
        n += 1
    
    for word in words:
        total = 0
        for letter in word:
            total += ord(letter) - ord("A") + 1
        if total in triangle_nums:
            count += 1
    
    return count

main()

#https://projecteuler.net/problem=42