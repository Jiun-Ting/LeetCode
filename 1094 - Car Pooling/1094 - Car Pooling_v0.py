class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        count = [0]*1001
        for trip in trips:
            count[trip[1]] += trip[0]
            count[trip[2]] -= trip[0]

        for i in count:
            capacity -= i
            if capacity < 0:
                return False
        return True
