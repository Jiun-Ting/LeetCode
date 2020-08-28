class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        s = set()
        Map =  collections.defaultdict(int)
        for i in nums:
            if i+k in Map:
                s.add(tuple(sorted([i+k, i])))
            if i-k in Map:
                s.add(tuple(sorted([i-k, i])))
            if i not in Map:
                Map[i] += 1
        return len(s)
