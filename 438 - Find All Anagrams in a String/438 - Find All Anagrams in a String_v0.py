from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        pC = Counter(p)
        sC = Counter(s[:len(p)])
        if pC==sC:
            ans.append(0)

        for i in range(1, len(s)-len(p)+1):
            sC[s[i-1]] -= 1
            sC[s[i+len(p)-1]] += 1
            if sC[s[i-1]] == 0:
                del sC[s[i-1]]
            if pC == sC:
                ans.append(i)
        return ans


        
