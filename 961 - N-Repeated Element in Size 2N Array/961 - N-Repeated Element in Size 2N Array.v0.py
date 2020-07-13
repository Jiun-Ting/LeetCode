class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = set()
        for i in A:
            if i in count:
                return i
            else:
                count.add(i)
