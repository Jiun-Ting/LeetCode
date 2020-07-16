class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = dict()
        for i in words:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        s = sorted(count.items(), key = lambda x: (-x[1], x[0]))
        ans = list()
        for i in s[:k]:
            ans.append(i[0])
        return ans
