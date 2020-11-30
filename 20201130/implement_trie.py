# https://leetcode.com/problems/implement-trie-prefix-tree/

class Node:
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None


class Trie:

    def __init__(self):
        self.root = None

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.root = self._insert(self.root, word)

    def _insert(self, node: Node, word: str):
        if node is None:
            return Node(word)
        elif word == node.value:
            return node
        elif word < node.value:
            node.left = self._insert(node.left, word)
        else:
            node.right = self._insert(node.right, word)
        return node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self._search(self.root, word)

    def _search(self, node: Node, word: str) -> bool:
        if not node:
            return False
        elif word == node.value:
            return True
        elif word < node.value:
            return self._search(node.left, word)
        else:
            return self._search(node.right, word)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._startsWith(self.root, prefix)

    def _startsWith(self, node: Node, prefix: str) -> bool:
        if not node:
            return False
        elif node.value.startswith(prefix):
            return True
        elif prefix < node.value:
            return self._startsWith(node.left, prefix)
        else:
            return self._startsWith(node.right, prefix)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)