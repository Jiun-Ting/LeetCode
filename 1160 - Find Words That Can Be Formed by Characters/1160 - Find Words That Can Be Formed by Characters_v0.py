class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        c_count = dict()
        for i in chars:
            if i in c_count:
                c_count[i] += 1
            else:
                c_count[i] = 1
        ans = 0
        for i in words:
            w_count = dict()
            for w in i:
                if w in w_count:
                    w_count[w] += 1
                else:
                    w_count[w] = 1
            Add = 1
            for k, v in w_count.items():
                if k not in c_count or c_count[k] < v:
                    Add = 0
                    break
            if Add:
                ans += len(i)
        return ans
