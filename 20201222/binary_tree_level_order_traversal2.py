# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

from typing import List
from common.common_data import TreeNode
from collections import deque


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        queue = deque()
        max_depth = 0

        def dfs(node: TreeNode, level: int):
            if not node: return

            nonlocal max_depth
            max_depth = max(level, max_depth)

            queue.append((node, level))
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        answer = [[] for _ in range(max_depth + 1)]

        while queue:
            node, level = queue.popleft()
            answer[max_depth - level].append(node.val)

        return answer

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        answer = []
        def dfs(node: TreeNode, level: int):
            if not node: return

            if level < len(answer):
                answer[level].append(node.val)
            else:
                answer.append([node.val])

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return reversed(answer)