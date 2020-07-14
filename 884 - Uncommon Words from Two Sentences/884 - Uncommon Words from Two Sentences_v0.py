class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a = A.split(" ")
        b = B.split(" ")
        ans = set()
        common = set()
        for i in a:
            if i not in ans and i not in common:
                ans.add(i)
            elif i in ans:
                ans.remove(i)
            common.add(i)
        for i in b:
            if i not in ans and i not in common:
                ans.add(i)
            elif i in ans:
                ans.remove(i)
            common.add(i)

        return list(ans)
