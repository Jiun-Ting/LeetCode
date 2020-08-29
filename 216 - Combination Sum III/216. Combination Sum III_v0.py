class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtrack(temp, start, end, total):
            if total == 0 and len(temp)==k:
                ans.append(temp[:])
            elif total > 0:
                for i in range(start, end):
                    if len(temp) <= k:
                        temp.append(i)
                        backtrack(temp, i+1, 10, total-i)
                        temp.pop()
        ans = []
        backtrack([], 1, 10, n)
        return ans
