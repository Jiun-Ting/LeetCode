class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        count_list = heapq.nlargest(k, [(v, k) for k, v in count.items()])
        ans = [i[1] for i in count_list]

        return ans
                    
