class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_str = str(n)
        num = set()
        num.add(n)

        while (1):
            if n_str == "1":
                return True
            Sum = 0
            for i in n_str:
                Sum += int(i)**2
            if Sum in num:
                return False
            else:
                num.add(Sum)
            n_str = str(Sum)
