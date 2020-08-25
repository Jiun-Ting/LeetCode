
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        n = len(nums)
        for Out in range(n-3):
            if Out > 0 and nums[Out-1] == nums[Out]: continue
            for L in range(Out+1, n-2):
                l, r = L+1, n-1
                if L > Out+1 and nums[L-1] == nums[L]: continue
                while l < r:
                    total = nums[Out]+nums[L]+nums[l]+nums[r]
                    if total == target:
                        ans.append([nums[Out],nums[L],nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif total > target:
                        r -= 1
                    else:
                        l += 1
        return ans
