class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l, r = 0, len(A)-1
        square = [i**2 for i in A]
        ans = [0]*len(A)
        n = len(A)-1
        while l <= r:
            if square[l] > square[r]:
                ans[n] = square[l]
                l += 1
            else:
                ans[n] = square[r]
                r -= 1
            n -= 1
        return ans
