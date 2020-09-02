class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        def DFS(i):
            time = 0
            for j in Map[i]:
                time =  max(time, informTime[i]+DFS(j))
            return time

        Map = collections.defaultdict(list)
        for i, v in enumerate(manager):
            Map[v].append(i)
        return DFS(headID)
