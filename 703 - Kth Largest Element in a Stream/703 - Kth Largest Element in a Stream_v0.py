import heapq as hq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.H = []
        self.K = k
        hq.heapify(self.H)
        for i in nums:
            hq.heappush(self.H, i)
            if len(self.H) > self.K:
                hq.heappop(self.H)
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        hq.heappush(self.H, val)
        if len(self.H) > self.K:
            hq.heappop(self.H)
        return self.H[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
