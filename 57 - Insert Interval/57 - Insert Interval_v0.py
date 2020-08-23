class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        insert = False
        if intervals == []:
            return [newInterval]
        for i in range(len(intervals)):
            if insert or newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                ans.append(intervals[i])
                insert = True
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInte\rval[1] = max(intervals[i][1], newInterval[1])
        if insert==False:
            ans.append(newInterval)
        if intervals[-1][1] > newInterval[1] and ans[-1] != intervals[-1]:
            ans.append(intervals[-1])
        return ans
