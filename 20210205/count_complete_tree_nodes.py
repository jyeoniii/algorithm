# https://leetcode.com/problems/count-complete-tree-nodes/

from common.common_data import TreeNode
from collections import deque


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        queue = deque([root])
        cnt = 0
        while queue:
            node = queue.popleft()
            cnt += 1
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return cnt
