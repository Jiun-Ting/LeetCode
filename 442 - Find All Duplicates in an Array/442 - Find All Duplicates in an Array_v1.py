class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(nums)
        for i in range(n):
            j = abs(nums[i])-1
            if nums[j] < 0:
                ans.append(j+1)
            else:
                nums[j] *= -1
        return ans
