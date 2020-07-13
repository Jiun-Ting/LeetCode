class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = [0]*102
        for i in nums:
            count[i+1] += 1

        for i in range(1, len(count)):
            count[i] += count[i-1]

        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = count[nums[i]]
        return ans
