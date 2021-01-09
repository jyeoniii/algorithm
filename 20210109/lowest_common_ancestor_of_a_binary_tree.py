# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


from common.common_data import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root.val: (root, 0)}  # parent[i] = parent of node i, depth of node i

        stack = [(root, 0)]
        while not p.val in parent or not q.val in parent:
            node, depth = stack.pop()
            if node.left:
                parent[node.left.val] = (node, depth+1)
                stack.append((node.left, depth+1))
            if node.right:
                parent[node.right.val] = (node, depth + 1)
                stack.append((node.right, depth+1))

        while parent[p.val][1] != parent[q.val][1]:
            if parent[p.val][1] < parent[q.val][1]: q = parent[q.val][0]
            else: p = parent[p.val][0]

        while p != q:
            p, q = parent[p.val][0], parent[q.val][0]

        return p