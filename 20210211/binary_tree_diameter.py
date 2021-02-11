# https://www.algoexpert.io/questions/Binary%20Tree%20Diameter


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    answer = 0
    def helper(node):
        nonlocal answer
        left = helper(node.left) + 1 if node.left else 0
        right = helper(node.right) + 1 if node.right else 0
        answer = max(answer, left + right)
        return max(left, right)

    helper(tree)
    return answer
