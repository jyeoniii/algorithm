# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/583/week-5-january-29th-january-31st/3621/

from common.common_data import TreeNode
from collections import defaultdict
from typing import List


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        depths, values = defaultdict(list), defaultdict(list)
        def helper(node: TreeNode, pos: int, depth: int):
            if not node: return

            i = len(depths[pos])-1
            while i >= 0 and (depths[pos][i] > depth or (depths[pos][i] == depth and values[pos][i] > node.val)): i -= 1
            values[pos] = values[pos][:i+1] + [node.val] + values[pos][i+1:]
            depths[pos] = depths[pos][:i+1] + [depth] + depths[pos][i+1:]

            helper(node.left, pos-1, depth+1)
            helper(node.right, pos+1, depth+1)

        helper(root, 0, 0)
        return list(map(lambda x: x[1], sorted(values.items(), key=lambda x: x[0])))


import bisect


class ValueAndDepth:
    def __init__(self, value: int, depth: int):
        self.value = value
        self.depth = depth

    def __lt__(self, other):
        return self.value < other.value if self.depth == other.depth else self.depth < other.depth


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = defaultdict(list)

        def helper(node: TreeNode, pos: int, depth: int):
            if not node: return
            bisect.insort(d[pos], ValueAndDepth(node.val, depth))

            helper(node.left, pos - 1, depth + 1)
            helper(node.right, pos + 1, depth + 1)

        helper(root, 0, 0)
        return [[vd.value for vd in li] for _, li in sorted(d.items(), key=lambda x: x[0])]


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = defaultdict(list)

        def helper(node: TreeNode, pos: int, depth: int):
            if not node: return
            bisect.insort(d[pos], [depth, node.val])

            helper(node.left, pos - 1, depth + 1)
            helper(node.right, pos + 1, depth + 1)

        helper(root, 0, 0)
        return [[vd.value for vd in li] for _, li in sorted(d.items(), key=lambda x: x[0])]


from collections import deque


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        q = deque([(root, 0, 0)]) # node, pos, depth
        d = defaultdict(list)

        while q:
            node, pos, depth = q.popleft()
            d[pos].append((depth, node.val))
            if node.left: q.append((node.left, pos-1, depth+1))
            if node.right: q.append((node.right, pos+1, depth+1))

        return [[dv[1] for dv in sorted(li)] for _, li in sorted(d.items(), key=lambda x: x[0])]
