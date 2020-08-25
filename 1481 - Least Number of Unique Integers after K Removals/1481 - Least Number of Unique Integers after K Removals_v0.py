class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        C = collections.Counter(arr)
        sorted_C = sorted(C.items(), key = lambda x:x[1])
        ans = len(sorted_C)
        i = 0
        while k > 0:
            k -= sorted_C[i][1]
            if k >= 0:
                ans -= 1
            i += 1

        return ans
