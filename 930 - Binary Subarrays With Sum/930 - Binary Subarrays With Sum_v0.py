class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        l = 0
        ans = 0
        count = 0
        for r, v in enumerate(A):
            S -= v
            if v == 1:
                count = 0
            while l <= r and S <= 0:
                if S == 0:
                    count += 1
                S += A[l]
                l += 1
            ans += count
        return ans
