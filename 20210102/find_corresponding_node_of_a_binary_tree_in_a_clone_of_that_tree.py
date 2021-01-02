# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3590/

from common.common_data import TreeNode
from collections import deque


# BFS
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q1 = deque([original])
        q2 = deque([cloned])
        while q1:
            node1, node2 = q1.popleft(), q2.popleft()
            if node1 == target:
                return node2

            if node1.left:
                q1.append(node1.left)
                q2.append(node2.left)

            if node1.right:
                q1.append(node1.right)
                q2.append(node2.right)


# DFS
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def helper(node1: TreeNode, node2: TreeNode) -> TreeNode:
            if node1 == target: return node2

            if node1.left:
                result = helper(node1.left, node2.left)
                if result: return result

            if node1.right:
                result = helper(node1.right, node2.right)
                if result: return result
        return helper(original, cloned)
