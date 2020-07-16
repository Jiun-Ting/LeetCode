class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(" ")
        if len(s) != len(pattern):
            return False

        c= dict()
        distinct = set()
        for i, v in enumerate(s):
            if pattern[i] not in c:
                if s[i] in distinct:
                    return False
                c[pattern[i]] = v
                distinct.add(v)
            elif pattern[i] in c and c[pattern[i]] != v:
                return False

        return True
