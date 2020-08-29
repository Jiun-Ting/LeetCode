class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(temp, start, end):
            if len(temp) == k:
                ans.append(temp[:])
            for i in range(start, end):
                if len(temp) < k:
                    temp.append(i)
                    backtrack(temp, i+1, end)
                    temp.pop()

        ans = []
        backtrack([], 1, n+1)
        return ans
