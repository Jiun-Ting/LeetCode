import heapq as hq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        Count = collections.Counter(nums)
        H = []
        hq.heapify(H)
        for K, V in Count.items():
            hq.heappush(H, (V, K))
            if len(H)>k:
                hq.heappop(H)
        return [i[1] for i in H]
