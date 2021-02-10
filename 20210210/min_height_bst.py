# https://www.algoexpert.io/questions/Min%20Height%20BST


def minHeightBst(array):
    if not array: return None

    mid = len(array) // 2
    node = BST(array[mid])
    node.left, node.right = minHeightBst(array[:mid]), minHeightBst(array[mid + 1:])
    return node

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
