# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

from common.common_data import TreeNode, ListNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        li = []
        while head:
            li.append(head.val)
            head = head.next

        def recursive(start: int, end: int) -> TreeNode:  # start, end: inclusive
            if start > end: return None

            mid = (start + end) // 2
            left = recursive(start, mid - 1)
            right = recursive(mid + 1, end)

            return TreeNode(li[mid], left, right)

        return recursive(0, len(li) - 1)

