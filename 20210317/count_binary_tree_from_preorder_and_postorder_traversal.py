# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

from typing import List
from common.common_data import TreeNode


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post: return None

        s1, s2, i = set(), set(), 0
        while i + 1 < len(pre) and i < len(post):
            s1.add(pre[i + 1])
            s2.add(post[i])
            if s1 == s2:
                break
            i += 1

        return TreeNode(
            pre[0],
            self.constructFromPrePost(pre[1:i + 2], post[:i + 1]),
            self.constructFromPrePost(pre[i + 2:], post[i + 1:-1])
        )


class Solution(object):
    def constructFromPrePost(self, pre, post):
        if not pre: return None
        elif len(pre) == 1: return TreeNode(pre[0])

        L = post.index(pre[1]) + 1
        return TreeNode(
            pre[0],
            self.constructFromPrePost(pre[1:L+1], post[:L]),
            self.constructFromPrePost(pre[L+1:], post[L:-1])
        )