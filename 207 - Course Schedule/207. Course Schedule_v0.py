class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def DFS(i):
            visit[i] = -1
            for j in Map[i]:
                if visit[j] == -1 or not DFS(j):
                    return False
                visit[j] = 1
            visit[i] = 1
            return True
        Map = collections.defaultdict(list)
        visit = [0]*numCourses
        for i in prerequisites:
            Map[i[0]].append(i[1])

        for i in range(numCourses):
            if not DFS(i):
                return False
        return True
