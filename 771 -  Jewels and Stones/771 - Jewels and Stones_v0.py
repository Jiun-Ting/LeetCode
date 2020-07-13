class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j = set()
        count = 0
        for item in J:
            j.add(item)
        for s in S:
            if s in j:
                count += 1
        return count
