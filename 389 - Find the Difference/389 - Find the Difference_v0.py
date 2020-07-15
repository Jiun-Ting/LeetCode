class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_list = [c for c in s]
        for c in t:
            if c not in s_list:
                return c
            else:
                s_list.remove(c)
