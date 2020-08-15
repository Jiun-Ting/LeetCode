class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        def bs(row):
            # find the smallest index where the element is 0
            l, r = 0, len(row)
            while l < r:
                mid = (l+r)//2
                if row[mid] == 0:
                    r = mid
                else:
                    l = mid + 1
            return l

        m, n = len(mat), len(mat[0])

        index = [(bs(mat[i]), i)  for i in range(m)]
        return [i for _, i in nsmallest(k, index)]
        
