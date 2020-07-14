class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = dict()
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        for k, v in count.items():
            if  v == 1:
                return k
            
