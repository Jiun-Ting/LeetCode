import heapq as hq
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        H = []
        hq.heapify(H)
        for i in set(nums):
            hq.heappush(H, i)
            if len(H) > 3:
                hq.heappop(H)
        if len(H) < 3:
            return H[-1]
        return H[0]
