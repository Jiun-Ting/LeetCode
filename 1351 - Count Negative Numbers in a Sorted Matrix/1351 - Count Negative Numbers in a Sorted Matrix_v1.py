class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # find the mininum index i where array[i] < 0

        m, n = len(grid), len(grid[0])
        ans = 0
        col = n-1
        for row in range(m):
            while grid[row][col] < 0 and col >= 0:
                col -= 1
            else:
                ans += n-(col+1)
        return ans
