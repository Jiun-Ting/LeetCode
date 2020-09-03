class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        d = collections.deque([])

        for i in range(min(k, len(nums))):
            while d:
                if nums[i] > nums[d[-1]]:
                    d.pop()
                else:
                    break
            d.append(i)

        ans = [nums[d[0]]]
        for i in range(k, len(nums)):
            while d:
                if nums[i] > nums[d[-1]]:
                    d.pop()
                else:
                    break
            if d and d[0] < i-k+1:
                d.popleft()
            d.append(i)
            ans.append(nums[d[0]])
        return ans
