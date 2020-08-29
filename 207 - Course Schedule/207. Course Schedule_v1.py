class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for i in range(numCourses)]
        degree = [0]*numCourses
        Pass = [False]*numCourses
        for i, j in prerequisites:
            graph[j].append(i)
            degree[i] += 1

        q = collections.deque([])
        for i, v in enumerate(degree):
            print(i)
            if v == 0:
                q.append(i)
                Pass[i] = True
        while q:
            pre = q.pop()
            for i in graph[pre]:
                degree[i] -= 1
                if degree[i] == 0:
                    q.append(i)
                    Pass[i] = True
        return sum(Pass) == numCourses
            
