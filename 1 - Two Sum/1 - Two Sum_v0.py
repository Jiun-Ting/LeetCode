class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = dict()
        for i, v in enumerate(nums):
            if target-v in table:
                return [i, table[target-v]]
            table[v] = i
