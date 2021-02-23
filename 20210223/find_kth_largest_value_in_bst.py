# https://www.algoexpert.io/questions/Find%20Kth%20Largest%20Value%20In%20BST


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    stack, node = [], tree
    while node:
        stack.append(node)
        node = node.right

    while stack:
        node = stack.pop()
        k -= 1
        if k == 0: return node.value
        if node.left:
            tmp = node.left
            while tmp:
                stack.append(tmp)
                tmp = tmp.right


def findKthLargestValueInBst(tree, k):
    visited_count, answer = 0, 0
    def helper(node):
        if not node: return
        nonlocal visited_count, answer

        helper(node.right)
        if visited_count >= k: return

        visited_count += 1
        if visited_count == k: answer = node.value

        helper(node.left)

    helper(tree)
    return answer
