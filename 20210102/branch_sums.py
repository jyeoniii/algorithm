# https://www.algoexpert.io/questions/Branch%20Sums


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    answer = []

    def helper(node, sum):
        if not node.left and not node.right:  # Leaf
            answer.append(sum + node.value)
            return

        if node.left: helper(node.left, sum + node.value)
        if node.right: helper(node.right, sum + node.value)

    helper(root, 0)
    return answer
