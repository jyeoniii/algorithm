# https://leetcode.com/problems/unique-binary-search-trees-ii/

from typing import List
from common.common_data import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return None
        def helper(left: int, right: int) -> List[TreeNode]: # [left, right)
            if left >= right: return [None]
            nodes = []
            for i in range(left, right):
                nodes.extend([TreeNode(i, l, r) for l in helper(left, i) for r in helper(i+1, right)])
            return nodes

        return helper(1, n+1)

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return None
        def helper(left: int, right: int) -> List[TreeNode]: # [left, right)
            if left >= right: return [None]
            return [TreeNode(i, l, r)
                    for i in range(left, right)
                    for l in helper(left, i)
                    for r in helper(i+1, right)]

        return helper(1, n+1)