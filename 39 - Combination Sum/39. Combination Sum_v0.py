class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(temp, start, end, Total):
            if Total == 0:
                ans.append(temp[:])
            elif Total > 0:
                for i in range(start, end):
                    temp.append(candidates[i])
                    backtrack(temp, i, end, Total-candidates[i])
                    temp.pop()

        ans = []
        backtrack([], 0, len(candidates), target)
        return ans
