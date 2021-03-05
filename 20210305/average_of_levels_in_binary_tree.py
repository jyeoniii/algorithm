# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3661/

from common.common_data import TreeNode
from typing import List
from collections import deque


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q, li = deque([(root, 0)]), []
        while q:
            node, depth = q.popleft()
            if depth < len(li):
                li[depth][0] += node.val
                li[depth][1] += 1
            else:
                li.append([node.val, 1])

            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

        return [value_sum / cnt for value_sum, cnt in li]


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        li = []

        def helper(node: TreeNode, level: int):
            if not node: return

            if level < len(li):
                li[level][0] += node.val
                li[level][1] += 1
            else:
                li.append([node.val, 1])
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        helper(root, 0)
        return [value_sum / cnt for value_sum, cnt in li]
