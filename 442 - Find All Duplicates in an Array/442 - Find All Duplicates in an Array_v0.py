class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        i, n = 0, len(nums)
        while i < n:
            j = nums[i]-1
            if j != i and nums[j] != nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
            else:
                i += 1
        for i, v in enumerate(nums):
            if i+1 != v:
                ans.append(v)
        return ans
