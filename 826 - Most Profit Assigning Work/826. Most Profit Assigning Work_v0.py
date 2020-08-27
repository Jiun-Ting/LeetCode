class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        s = sorted(zip(difficulty, profit), key = lambda x:x[0])
        worker.sort()
        pairs = [s[0]]
        for i in range(1, len(s)):
            if s[i][0] >= pairs[-1][0] and s[i][1] >= pairs[-1][1]:
                pairs.append(s[i])

        p = 0
        ans = 0
        for w in range(len(worker)):
            while p+1 < len(pairs) and pairs[p+1][0] <= worker[w]:
                p += 1
            if pairs[p][0] <= worker[w]:
                ans += pairs[p][1]
        return ans
