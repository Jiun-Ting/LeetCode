class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        s_count = sorted(count.items(), key = lambda x: -x[1])
        print(s_count)
        ans = ""
        for i in s_count:
            ans+=i[0]*i[1]
        return ans
