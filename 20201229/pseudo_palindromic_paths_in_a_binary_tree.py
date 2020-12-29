# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3585/

from common.common_data import TreeNode
from typing import List
from collections import Counter, defaultdict


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def helper(node: TreeNode, path: List[int]) -> int:  # node should not be None
            if not node.left and not node.right:
                counter = Counter(path)
                return 1 if 0 <= sum(x % 2 for x in counter.values()) <= 1 else 0
            else:
                answer = 0
                if node.left:
                    path.append(node.left.val)
                    answer += helper(node.left, path)
                    path.pop()
                if node.right:
                    path.append(node.right.val)
                    answer += helper(node.right, path)
                    path.pop()
                return answer

        return helper(root, [root.val])


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        counter = defaultdict(int)
        def helper(node: TreeNode) -> int:  # node should not be None
            if not node: return 0

            counter[node.val] += 1
            if not node.left and not node.right:
                answer = 1 if 0 <= sum(x % 2 for x in counter.values()) <= 1 else 0
            else:
                answer = helper(node.left) + helper(node.right)

            counter[node.val] -= 1
            return answer

        return helper(root)