class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        S = list(s)
        i = 0
        while i < len(S):
            j = indices[i]
            if indices[i] != indices[j]:
                S[i], S[j] = S[j], S[i]
                indices[i], indices[j] = indices[j], indices[i]
            else:
                i += 1
        return "".join(S)
