class StockSpanner(object):

    def __init__(self):
        self.s = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        ans = 1
        while self.s and self.s[-1][0] <= price:
            _, count = self.s.pop()
            ans += count
        self.s.append((price, ans))
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
