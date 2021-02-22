# https://www.algoexpert.io/questions/Suffix%20Trie%20Construction


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for j in range(len(string ) -1, -1, -1):
            children = self.root
            for i in range(j, len(string)):
                c = string[i]
                if c not in children:
                    children[c] = {}
                children = children[c]
            children['*'] = True

    def contains(self, string):
        children = self.root
        for c in string:
            if c not in children:
                return False
            else:
                children = children[c]
        return '*' in children

