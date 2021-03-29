# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/592/week-5-march-29th-march-31st/3689/

from common.common_data import TreeNode
from typing import List


class Solution:

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        answer, cnt, impossible = [], 0, False

        def helper(node: TreeNode):
            nonlocal impossible, cnt
            if not node or impossible: return
            if node.val != voyage[cnt]:
                impossible = True
                return

            cnt += 1
            if cnt >= len(voyage) or not node.left and not node.right: return
            if node.left:
                if voyage[cnt] == node.left.val:
                    helper(node.left)
                    helper(node.right)
                else:
                    answer.append(node.val)
                    helper(node.right)
                    helper(node.left)
            else:
                helper(node.right)

        helper(root)
        return [-1] if impossible else answer


