class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        change = 0
        furthest = 0
        ans = 0
        for i in range(n):
            furthest = max(furthest, nums[i]+i)
            if i == change:
                ans += 1
                change = furthest
                if change >= n-1:
					break
        return ans
