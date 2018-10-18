'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
'''
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        f = [True for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            f[pre[0]] = False
            graph[pre[0]].append(pre[1])
        def find(i,l):
            if f[i]:
                return True
            if i in l:
                return False
            l.append(i)
            for g in graph[i]:
                if not find(g,l):
                    return False
            return True

        for i in range(0, numCourses):
            if graph[i]:
                l = []
                if not find(i,l):
                    return False
            f[i] = True
        return True