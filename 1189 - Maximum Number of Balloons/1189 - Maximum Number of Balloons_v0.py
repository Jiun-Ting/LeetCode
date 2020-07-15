class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = collections.defaultdict(int)
        for i in text:
            count[i] += 1
        count_input = collections.Counter('balloon')
        ans = len(text)
        for k, v in count_input.items():
            ans = min(ans, count[k]/v)
        return ans
