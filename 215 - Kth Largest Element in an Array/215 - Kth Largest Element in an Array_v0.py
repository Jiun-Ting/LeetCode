import heapq as hq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        H = []
        hq.heapify(H)
        for i in nums:
            hq.heappush(H, i)
            if len(H) > k:
                hq.heappop(H)
        return hq.heappop(H)
        
