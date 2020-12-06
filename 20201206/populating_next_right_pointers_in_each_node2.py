# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3556/

from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None

        queue = deque([(root)])
        while queue:
            node = queue.popleft()
            nodes = [node]
            while queue:
                nodes.append(queue.popleft())
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i+1]

            for node in nodes:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root