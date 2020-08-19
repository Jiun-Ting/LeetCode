import heapq as hq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        H = []
        hq.heapify(H)
        for s in stones:
            hq.heappush(H, -s)
        while len(H) > 1:
            x = hq.heappop(H)
            y = hq.heappop(H)
            if y-x > 0:
                hq.heappush(H, x-y)
        if len(H) == 0:
            return 0
        else:
            return -hq.heappop(H)
