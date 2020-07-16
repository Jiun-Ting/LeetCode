class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d = dict()
        t_set = set()
        for i, v in enumerate(s):
            if v not in d:
                if t[i] in t_set:
                    return False
                else:
                    d[v] = t[i]
                    t_set.add(t[i])
            elif v in d and d[v] != t[i]:
                return False
        return True
