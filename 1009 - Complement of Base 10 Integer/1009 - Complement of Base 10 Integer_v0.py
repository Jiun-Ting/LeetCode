class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        mask = 1
        while mask < N:
            mask = (mask << 1) +1
        return mask^N
