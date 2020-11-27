# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/
# BFS

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        answer = []
        if root:
            queue.append((root, 0))

        while queue:
            (node, level) = queue.pop(0)
            if len(answer) - 1 < level:
                answer.append([])
            answer[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        for idx, l in enumerate(answer):
            if idx % 2 != 0:
                l.reverse()
        return answer

# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return None
#
#         q = deque([root])
#         temp = []
#         flag = 1
#         result = []
#
#         while q:
#             for _ in range(len(q)):
#                 curr = q.popleft()
#                 temp.append(curr.val)
#                 if curr.left:
#                     q.append(curr.left)
#                 if curr.right:
#                     q.append(curr.right)
#
#             result.append(temp[::flag])
#             temp = []
#             flag = flag * (-1)
#         return result
