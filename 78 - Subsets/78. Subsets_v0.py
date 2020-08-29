class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(temp, start, end):
            ans.append(temp[:])
            for i in range(start, end):
                temp.append(nums[i])
                backtrack(temp, i+1, end)
                temp.pop()

        ans = []
        backtrack([], 0, len(nums))

        return ans
