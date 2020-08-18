class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        total =0
        ans = len(nums)+1
        for j, v in enumerate(nums):
            total += v
            while total >= s and i < len(nums):
                total -= nums[i]
                ans = min(ans, j-i+1)
                i += 1
        if ans < len(nums)+1:
            return ans
        return 0
