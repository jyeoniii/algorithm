# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        listA = []
        listB = []
        node = headA
        while node:
            listA.append(node)
            node = node.next
        node = headB
        while node:
            listB.append(node)
            node = node.next

        answer, cond = None, True
        while cond:
            nodeA = listA.pop() if listA else None
            nodeB = listB.pop() if listB else None
            cond = nodeA and nodeB and nodeA == nodeB
            if cond:
                answer = nodeA

        return answer


"""
Faster solution (Find same reference)
"""
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         d = {}
#         node = headA
#         while node:
#             d[node] = True
#             node = node.next
#
#         node = headB
#         while node:
#             if node in d:
#                 return node
#             node = node.next
#
#         return None