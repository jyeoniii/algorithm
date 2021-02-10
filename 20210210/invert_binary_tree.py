# https://www.algoexpert.io/questions/Invert%20Binary%20Tree


def invertBinaryTree(tree):
    if not tree: return None

    left = invertBinaryTree(tree.left)
    right = invertBinaryTree(tree.right)
    tree.left, tree.right = right, left
    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
