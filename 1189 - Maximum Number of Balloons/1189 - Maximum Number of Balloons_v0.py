class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = collections.defaultdict(int)
        for i in text:
            count[i] += 1
        return min(count["b"], count["a"], count["l"]/2, count["o"]/2, count["n"])
