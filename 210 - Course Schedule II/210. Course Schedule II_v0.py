class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for i in range(numCourses)]
        degree = [0]*numCourses
        for i, j in prerequisites:
            graph[j].append(i)
            degree[i] += 1

        q = collections.deque([])
        for i, v in enumerate(degree):
            if v == 0:
                q.append(i)
        ans = []
        while q:
            pre = q.pop()
            ans.append(pre)
            for i in graph[pre]:
                degree[i] -= 1
                if degree[i] == 0:
                    q.append(i)

        if len(ans) < numCourses:
            return []
        return ans
