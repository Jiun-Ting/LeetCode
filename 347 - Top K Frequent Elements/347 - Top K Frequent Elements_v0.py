class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums).most_common()
        ans = []
        for i in range(k):
            ans.append(count[i][0])
        return ans
                    
