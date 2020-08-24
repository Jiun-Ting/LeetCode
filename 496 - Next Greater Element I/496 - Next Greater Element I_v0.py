class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        D = collections.defaultdict(int)
        s = []
        for i in range(len(nums2)):
            while s and s[-1] < nums2[i]:
                v = s.pop()
                D[v] = nums2[i]
            s.append(nums2[i])
        ans = [-1]*len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in D:
                ans[i] = D[nums1[i]]
        return ans
