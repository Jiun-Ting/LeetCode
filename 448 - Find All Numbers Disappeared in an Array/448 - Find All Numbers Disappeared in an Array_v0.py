class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums:
            j = abs(i)-1
            if nums[j] > 0:
                nums[j] = -nums[j]
        for i, v in enumerate(nums):
            if v > 0:
                ans.append(i+1)
        return ans
