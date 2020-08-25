class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = []
        n = len(nums)
        ans = [-1]*n
        for i in range(2*n):
            while s and s[-1][0] < nums[i%n]:
                v, index = s.pop()
                ans[index] = nums[i%n]
            if i < n:
                s.append((nums[i%n], i))
        return ans
