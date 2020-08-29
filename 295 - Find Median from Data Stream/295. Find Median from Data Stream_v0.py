import heapq as hq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Min = []
        self.Max = []
        hq.heapify(self.Min)
        hq.heapify(self.Max)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.Min) == 0 or self.Min[0] < num:
            hq.heappush(self.Min, num)
        else:
            hq.heappush(self.Max, -num)


        if len(self.Min) > len(self.Max)+1:
            hq.heappush(self.Max, -hq.heappop(self.Min))

        elif len(self.Max) > len(self.Min)+1:
            hq.heappush(self.Min, -hq.heappop(self.Max))


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.Min) == len(self.Max):
            return float(self.Min[0])/2 - float(self.Max[0])/2
        elif len(self.Min) > len(self.Max):
            return self.Min[0]
        else:
            return -self.Max[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
