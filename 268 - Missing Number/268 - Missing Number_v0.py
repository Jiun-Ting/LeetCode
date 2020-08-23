class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        XOR = 0
        for i in nums:
            XOR ^= i
        for i in range(len(nums)+1):
            XOR ^= i
        return XOR
