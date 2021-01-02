# https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST


def findClosestValueInBst(tree, target):
    if tree.value == target: return target

    left = findClosestValueInBst(tree.left, target) if tree.left else float("inf")
    right = findClosestValueInBst(tree.right, target) if tree.right else float("inf")

    left_diff, right_diff, curr_diff = abs(target - left), abs(target - right), abs(target - tree.value)
    if left_diff < right_diff and left_diff < curr_diff: return left
    elif right_diff < left_diff and right_diff < curr_diff: return right
    else: return tree.value


def findClosestValueInBst(tree, target):
    def helper(node, target, closest):
        if abs(target - closest) > abs(target - node.value): closest = node.value

        if node.left and target < node.value:
            return helper(node.left, target, closest)
        if node.right and target > node.value:
            return helper(node.right, target, closest)
        return closest

    return helper(tree, target, tree.value)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
