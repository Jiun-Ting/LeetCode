class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        s = heapq.nsmallest(k, count.items(), key=lambda x:(-x[1], x[0]))

        return [i[0] for i in s]
      
