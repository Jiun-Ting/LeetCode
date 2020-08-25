class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        Min = 10**6
        Max = 10**3
        ans = 0
        for s in salary:
            Min = min(Min, s)
            Max = max(Max, s)
            ans += s

        return float(ans-Min-Max)/(len(salary)-2)
