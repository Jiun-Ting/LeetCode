class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l, r = 0, len(letters)-1
        if target >= letters[r]:
            return letters[0]
        while l < r:
            mid = (l+r)/2
            if letters[mid] > target:
                r = mid
            else:
                l = mid +1
        return letters[l]
