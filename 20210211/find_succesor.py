# https://www.algoexpert.io/questions/Find%20Successor

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    else:
        p = node.parent
        while p and p.right == node:
            p = p.parent
            node = p
        return p
