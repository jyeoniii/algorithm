# https://leetcode.com/problems/course-schedule-ii/

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        incomings, outgoings = [0 for _ in range(numCourses)], [[] for _ in range(numCourses)]
        for course, pre_course in prerequisites:
            incomings[course] += 1
            outgoings[pre_course].append(course)

        queue = []
        for idx, incomings_count in enumerate(incomings):
            if incomings_count == 0:
                queue.append(idx)

        result = []
        while queue:
            course = queue.pop()
            result.append(course)
            for next in outgoings[course]:
                incomings[next] -= 1
                if incomings[next] == 0:
                    queue.append(next)

        return result if len(result) == numCourses else []
