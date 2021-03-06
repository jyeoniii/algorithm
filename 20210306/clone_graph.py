# https://leetcode.com/problems/clone-graph/

from common.common_data import Node


class Solution:
    def __init__(self):
        self.map = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None

        newNode = Node(node.val)
        self.map[node] = newNode
        newNode.neighbors = [self.map[n] if n in self.map else self.cloneGraph(n) for n in node.neighbors]

        return newNode

