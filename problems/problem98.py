from itertools import combinations
from math import floor, ceil
import numpy as np

def main():
    words = read_file("../data/p098_words.txt")
    anagram_groups = [x for x in anagrams(words) if len(x) >= 2]
    max_len = max(len(x[0]) for x in anagram_groups)
    squares = np.array([x**2 for x in range(int(10**(max_len/2)))])

    largest = 0 
    for group in anagram_groups:
        for a1, a2 in combinations(group, 2):
            pattern = word_pattern(a1)
            sub_squares = set(squares[(squares >= 10**(len(a1)-1)) & (squares < 10**(len(a1)))]) # Square numbers with same length as a1, a2
            for square in sub_squares:
                str_square = str(square)
                if pattern != word_pattern(str_square):
                    continue
                perm = get_permutation(a1, a2)
                perm_square = int(apply_permutation(perm, str_square))
                if perm_square in sub_squares:
                    largest = max(largest, square, perm_square)
    print(largest)
               
def anagrams(word_list):
    groups = {}
    for word in word_list:
        id = char_counts(word)
        if id in groups:
            groups[id].append(word)
        else:
            groups[id] = [word]
    return groups.values()

def char_counts(word):
    counts = []
    for c in set(word):
        counts.append((c, word.count(c)))
    return tuple(sorted(counts))

def word_pattern(word):
    return [word.index(c) for c in word]

def get_permutation(word1, word2):
    perm = []
    for c1 in word1:
        for i, c2 in enumerate(word2):
            if c1 == c2 and i not in perm:
                perm.append(i)
                break
    return perm

def apply_permutation(perm, word):
    out = [0 for _ in range(len(word))]
    for i, j in enumerate(perm):
        out[j] = word[i]
    return "".join(out)

def read_file(file):
    with open(file) as f:
        return f.read()[1:-1].split('","')

if __name__ == "__main__":
    main()