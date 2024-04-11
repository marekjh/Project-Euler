from itertools import combinations

def main():
    # words = read_file("../data/p098_words.txt")
    # max_num = 0
    # for anagram in anagrams(words):
    #     num = square_num(anagram)
    #     if num > max_num:
    #         max_num = num
    # print(max_num)
    nums = []
    for n in range(1, int(1_000_000_000**0.5)+1):
        nums.append(str(n**2))
    for anagram in anagrams(nums):
        if len(anagram) >= 2:
            print(anagram)

def anagrams(word_list):
    groups = {}
    for word in word_list:
        id = word_pattern(word)
        if id in groups:
            groups[id].add(word)
        else:
            groups[id] = {word}
    return groups.values()

def word_pattern(word):
    pattern = []
    for c in set(word):
        pattern.append((c, word.count(c)))
    return tuple(sorted(pattern, key=lambda x: x[0]))

def read_file(file):
    with open(file) as f:
        return f.read()[1:-1].split('","')

if __name__ == "__main__":
    main()