# https://leetcode.com/problems/all-paths-from-source-to-target/

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        def helper(vid: int, li: List[int]):
            li.append(vid)
            if vid == len(graph)-1:
                answer.append(li[:])
            else:
                for conn_vid in graph[vid]: helper(conn_vid, li)
            li.pop()
        helper(0, [])
        return answer