class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # find the mininum index i where array[i] < 0
        def bs(array):
            l, r = 0, n
            if array[n-1] >= 0:
                return n
            while l < r:
                mid =  (l+r)//2
                if array[mid] < 0:
                    r = mid
                else:
                    l = mid + 1
            return l
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            ans += n - bs(grid[i])
            print(ans, bs(grid[i]))
        return ans
