class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max = (1, -1)
        for i, v in enumerate(nums):
            if  v >= Max[0]:
                Max = (v, i)
        Second = (1, -1)
        for i, v in enumerate(nums):
            if i != Max[1] and v >= Second[0]:
                Second = (v, i)
        return (Max[0]-1)*(Second[0]-1)
