# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3630/

from common.common_data import TreeNode
from typing import List
from collections import defaultdict


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        d = defaultdict(list)

        def helper(node: TreeNode, depth: int):
            if not node: return
            d[depth].append(node.val)
            helper(node.left, depth+1)
            helper(node.right, depth+1)

        helper(root, 0)
        return [d[x][-1] for x in d]


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        d = {}

        def helper(node: TreeNode, depth: int):
            if not node: return
            d[depth] = node.val
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)

        helper(root, 0)
        return d.values()