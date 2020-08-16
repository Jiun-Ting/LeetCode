class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        path = [0]*(len(cost)+1)    
        for i in range(2, len(cost)+1):
            path[i] = min(path[i-1] + cost[i-1], path[i-2] + cost[i-2])
        return path[-1]
