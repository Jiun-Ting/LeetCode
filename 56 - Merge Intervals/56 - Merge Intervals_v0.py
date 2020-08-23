class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, n = 0, len(nums)
        if n == 0: return 1
        while i < n:
            j = nums[i]-1
            if j != i and j < n and j >= 0 and nums[j]!= nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return i+2
