class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newTail = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[newTail-1] != nums[i]:
                nums[newTail] = nums[i]
                newTail += 1
                count = 1
            elif count < 2:
                nums[newTail] = nums[i]
                newTail += 1
                count += 1
            else:
                count += 1
        return newTail
