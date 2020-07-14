class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        Line = dict()
        for i in "qwertyuiop":
            Line[i] = 1
        for i in "asdfghjkl":
            Line[i] = 2
        for i in "zxcvbnm":
            Line[i] = 3

        ans = []
        for word in words:
            line = set()
            for char in word.lower():
                line.add(Line[char])
            if len(line) <= 1:
                ans.append(word)
        return ans
