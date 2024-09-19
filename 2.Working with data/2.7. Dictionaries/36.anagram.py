from collections import defaultdict


def find_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())


words = ['eat', 'ate', 'tea', 'bat', 'tab', 'gut', 'tug', 'cat', 'act']
anagram_groups = find_anagrams(words)
for group in anagram_groups:
    print(group)
