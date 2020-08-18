class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        ans = 0
        count = 0
        for r, v in enumerate(nums):
            if v%2 == 1:
                k -= 1
                count = 0
            while k <= 0 and l <= r:
                if  k == 0:
                    count += 1
                if nums[l]%2 == 1:
                    k += 1
                l += 1
            ans += count
        return ans
