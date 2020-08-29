class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(temp, start, end):
            ans.append(temp[:])

            for i in range(start, end):
                if i > start and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                backtrack(temp, i+1, end)
                temp.pop()

        ans = []
        nums.sort()
        backtrack([], 0, len(nums))
        return ans
