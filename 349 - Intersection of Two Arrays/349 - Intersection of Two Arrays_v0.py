class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        N1 = set(nums1)
        N2 = set(nums2)
        ans = list()
        if len(N1) < len(N2):
            for i in N1:
                if i in N2:
                    ans.append(i)
        else:
            for i in N2:
                if i in N1:
                    ans.append(i)
        return ans
