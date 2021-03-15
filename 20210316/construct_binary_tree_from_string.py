# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3672/

from common.common_data import TreeNode


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s: return None

        i = 0
        while i < len(s) and s[i] != '(': i += 1
        root_val = int(s[:i])

        cnt, j = 0, i
        while j < len(s):
            if s[j] == '(':
                cnt += 1
            elif s[j] == ')':
                cnt -= 1
                if cnt == 0:
                    break
            j += 1

        left, right = self.str2tree(s[i + 1:j]), self.str2tree(s[j + 2:-1])
        return TreeNode(root_val, left, right)


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        def helper(idx: int) -> (TreeNode, int):
            if idx == len(s): return None, idx

            start_idx = idx
            while idx < len(s) and (s[idx] != '(' and s[idx] != ')'):
                idx += 1

            node = TreeNode(int(s[start_idx:idx]))

            if idx == len(s):
                return node, idx
            elif s[idx] == '(':
                node.left, idx = helper(idx + 1)
                if idx < len(s) and s[idx] == '(':
                    node.right, idx = helper(idx + 1)

            return node, idx + 1

        return helper(0)[0]


