class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = dict()
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        ans = 0
        for _ , v in count.items():
             ans += (1+(v-1))*(v-1)/2
        return ans
