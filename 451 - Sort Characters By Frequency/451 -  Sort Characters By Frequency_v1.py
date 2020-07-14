class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_bucketSort = collections.Counter(s).most_common()
        ans = ""
        for i in count_bucketSort :
            ans+=i[0]*i[1]
        return ans
