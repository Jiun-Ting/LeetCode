class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.defaultdict(int)
        for i in s:
            count[i] += 1

        ans = 0
        flag = 0
        for _, v in count.items():
            if v%2 == 0:
                ans += v
            else:
                flag = 1
                ans += v-1
        if flag:
            ans += 1

        return ans
