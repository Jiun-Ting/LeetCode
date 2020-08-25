class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        Min = (abs(nums[0]+nums[1]+nums[n-1]-target),  nums[0]+nums[1]+nums[n-1])
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                total = nums[i]+nums[l]+nums[r]
                if  abs(total-target) < Min[0]:
                    Min = (abs(total-target), total)
                if total == target:
                    return target
                elif total > target:
                    r -= 1
                else:
                    l += 1

        return Min[1]
