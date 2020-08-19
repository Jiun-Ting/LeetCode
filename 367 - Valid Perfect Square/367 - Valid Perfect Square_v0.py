class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num
        while l < r:
            mid = (l+r)//2
            if mid**2 >= num:
                r = mid
            else:
                l = mid + 1

        if l**2 == num:
            return True
        else:
            return False
