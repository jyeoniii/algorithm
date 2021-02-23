# https://www.algoexpert.io/questions/Group%20Anagrams

from collections import defaultdict


def groupAnagrams(words):
    d = defaultdict(list)
    for word in words:
        counter = [0] * 26
        for c in word:
            counter[ord(c) - ord('a')] += 1

        d[''.join(str(x) for x in counter)].append(word)
    return list(d.values())


def groupAnagrams(words):
    d = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        d[sorted_word].append(word)
    return list(d.values())
