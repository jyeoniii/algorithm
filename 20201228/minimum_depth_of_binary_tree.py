# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from common.common_data import TreeNode


# DFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0:
            return right + 1
        elif right == 0:
            return left + 1
        else:
            return min(left, right) + 1


from collections import deque


# BFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        q = deque([(root, 1)])

        while q:  # BFS
            node, depth = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
