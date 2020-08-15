class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])== 0:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while l < r:
            mid = (l + r)//2
            if matrix[mid//n][mid%n] >= target:
                r = mid
            else:
                l = mid + 1
        if matrix[l//n][l%n] == target:
            return True
        return False
