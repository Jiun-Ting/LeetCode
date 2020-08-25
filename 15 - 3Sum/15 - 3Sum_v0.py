class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        n = len(nums)
        for L in range(n-2):
            if nums[L] > 0: break
            l, r = L+1, n-1
            if L > 0 and nums[L] == nums[L-1]:
                continue
            while l < r:
                if -nums[L] == nums[l]+nums[r]:
                    ans.append([nums[L], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                    l += 1
                elif -nums[L] > nums[l]+nums[r]:
                    l += 1
                else:
                    r -= 1
        return ans
