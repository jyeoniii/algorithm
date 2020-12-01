# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3551/
# December Leetcode challenge Day1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        answer = 0

        def dfs(node: TreeNode, depth: int):
            if not node: return

            nonlocal answer
            answer = max(answer, depth)
            if node.left: dfs(node.left, depth + 1)
            if node.right: dfs(node.right, depth + 1)

        dfs(root, 1)
        return answer