class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        s = list()
        ans = [0]*len(T)
        for i in range(len(T)):
            while s and T[i] > s[-1][0]:
                n = s.pop()
                ans[n[1]] = i-n[1]
            s.append((T[i], i))
        return ans
