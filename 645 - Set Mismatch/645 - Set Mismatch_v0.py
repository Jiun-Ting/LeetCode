class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b = [0]*(len(nums)+1)
        for i, v in enumerate(nums):
            b[v] += 1
        ans = [0]*2
        for i, v in enumerate(b):
            print(i, v)
            if v==2:
                ans[0] = i
            if v==0:
                ans[1] = i
        return ans
        
