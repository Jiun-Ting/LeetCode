class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        Max = (r - l)*min(height[l], height[r])
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            Max = max(Max, (r - l)*min(height[l], height[r]))
        return Max
