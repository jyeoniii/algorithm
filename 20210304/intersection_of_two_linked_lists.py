# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3660/

from common.common_data import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next

        while headB:
            if headB in s:
                return headB
            headB = headB.next

        return None


class Solution:
    def getLength(self, node: ListNode):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = self.getLength(headA), self.getLength(headB)

        if lenA > lenB:
            for _ in range(lenA - lenB): headA = headA.next
        else:
            for _ in range(lenB - lenA): headB = headB.next

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA