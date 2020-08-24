import heapq as hq
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        H = []
        hq.heapify(H)
        for point in points:
            hq.heappush(H, (-(point[0]**2+point[1]**2), point))
            if len(H) > K:
                hq.heappop(H)

        return [i[1] for i in H]
