# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self, c: chr):
        self.c = c
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode('.') # root dummy node

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.children['!'] = TrieNode('!') # Mark finished

    def search(self, word: str) -> bool:
        return self._search(self.trie, word, 0)

    def _search(self, node: TrieNode, word: str, idx: int=0):
        if idx == len(word):
            return '!' in node.children
        if word[idx] == '.':
            for child in node.children:
                if self._search(node.children[child], word, idx+1): return True
        elif word[idx] in node.children:
            return self._search(node.children[word[idx]], word, idx+1)
        else:
            return False


