# https://programmers.co.kr/learn/courses/30/lessons/60060

def solution(words, queries):
    def matches(word, query):
        if len(query) != len(word): return False

        if query.startswith('?'):
            for i, c in enumerate(query):
                if c != '?':
                    return word[i:] == query[i:]
            return True  # All characters are '?'
        else:
            for i, c in enumerate(query):
                if c == '?':
                    return word[:i] == query[:i]
            return False  # All characters are alphabet, which will never happen

    return list(map(lambda query: [matches(word, query) for word in words].count(True), queries))


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.cnt = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TreeNode(None)

    def insert(self, s):
        node = self.root
        for c in s:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = TreeNode(c)
                node = node.children[c]
            node.cnt += 1

    def starts_with_count(self, keyword):
        node = self.root
        for c in keyword:
            if c in node.children:
                node = node.children[c]
            else:
                return 0
        return node.cnt


def solution(words, queries):
    trie = [Trie() for _ in range(10000)]
    reversed_trie = [Trie() for _ in range(10000)]

    for word in words:
        trie[len(word)-1].insert(word)
        reversed_trie[len(word)-1].insert(word[::-1])

    def matches_count(query: str):
        if query.startswith('?'):
            for i, c in enumerate(query):
                if c != '?':
                    return reversed_trie[len(query)-1].starts_with_count(query[i:][::-1])
            return reversed_trie[len(query)-1].root.cnt
        else:
            for i, c in enumerate(query):
                if c == '?':
                    return trie[len(query)-1].starts_with_count(query[:i])

    return list(map(lambda query: matches_count(query), queries))


if __name__ == "__main__":
    print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))