class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        s = []
        for i in range(len(prices)):
            while s and s[-1][0] >= prices[i]:
                p, j= s.pop()
                prices[j] = p-prices[i]
            s.append((prices[i], i))

        return prices
