class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        words = dict()
        for i in arr:
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1
        num = set()
        for _, value in words.items():
            if value not in num:
                num.add(value)
            else:
                return False
        return True
