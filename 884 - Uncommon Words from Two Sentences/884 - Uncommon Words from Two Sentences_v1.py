class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        c = (A+" "+B).split(" ")
        count = collections.Counter(c)
        ans = list()
        for k, v in count.items():
            if v == 1:
                ans.append(k)
        return ans
