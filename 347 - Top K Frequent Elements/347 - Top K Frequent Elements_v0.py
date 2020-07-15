class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums).most_common(k)
        ans = []
        for i in count:
            ans.append(i[0])
        return ans
                    
