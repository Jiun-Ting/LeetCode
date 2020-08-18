class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        l = 0
        ans = 0
        for r, v in enumerate(A):
            if v == 0:
                K -= 1
            while K < 0 and l < len(A):
                if A[l] == 0:
                    K += 1
                l += 1
            ans = max(ans, r-l+1)
        return ans
