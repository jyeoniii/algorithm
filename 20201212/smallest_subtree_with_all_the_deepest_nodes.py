# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3563/

from common.common_data import TreeNode
from functools import reduce


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root: return None

        parent, depth = {}, {}
        leaf_nodes = []
        max_depth = 0

        def dfs(node: TreeNode, d: int):
            nonlocal max_depth

            depth[node.val] = d
            max_depth = max(max_depth, d)

            if node.left:
                parent[node.left.val] = node
                dfs(node.left, d + 1)
            if node.right:
                parent[node.right.val] = node
                dfs(node.right, d + 1)
            if not node.left and not node.right: # leaf node
                leaf_nodes.append((node, d))

        def find_lca(x: TreeNode, y: TreeNode) -> TreeNode:
            while depth[x.val] != depth[y.val]:
                if depth[x.val] > depth[y.val]:
                    x = parent[x.val]
                elif depth[x.val] < depth[y.val]:
                    y = parent[y.val]
            if x == y: return x

            while parent[x.val] != parent[y.val]:
                x, y = parent[x.val], parent[y.val]

            return parent[x.val]

        dfs(root, 0)
        deepest_nodes = map(lambda x: x[0], filter(lambda x: x[1] == max_depth, leaf_nodes))

        return reduce(lambda acc, curr: find_lca(acc, curr), deepest_nodes)
