class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = dict()
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i in t:
            if i not in count:
                return False
            else:
                count[i] -= 1

        for _, v in count.items():
            if v != 0:
                return False

        return True
