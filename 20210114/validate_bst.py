# https://www.algoexpert.io/questions/Validate%20BST


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    answer = True
    def helper(node):
        nonlocal answer
        if node.left and node.right:
            left_min, left_max = helper(node.left)
            right_min, right_max = helper(node.right)
            if not left_max < node.value <= right_min: answer = False
            return left_min, right_max
        elif node.left:
            left_min, left_max = helper(node.left)
            if not left_max < node.value: answer = False
            return left_min, node.value
        elif node.right:
            right_min, right_max = helper(node.right)
            if not node.value <= right_min: answer = False
            return node.value, right_max
        else:
            return node.value, node.value

    helper(tree)
    return answer


def validateBst(tree):
    def helper(node, min, max):
        if not node: return True
        return min <= node.value < max and helper(node.left, min, node.value) and helper(node.right, node.value, max)

    return helper(tree)