class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums, reverse=True)
        rest = sum(nums)
        Sum = 0
        ans = []
        for i in nums:
            Sum += i
            rest -= i
            ans.append(i)
            if Sum > rest:
                break
        return ans
