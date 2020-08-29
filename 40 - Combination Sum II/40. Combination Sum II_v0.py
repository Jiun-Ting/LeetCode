class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(temp, start, end, total):
            if total == 0:
                ans.append(temp[:])
            elif total > 0:
                for i in range(start, end):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    temp.append(candidates[i])
                    backtrack(temp, i+1, end, total-candidates[i])
                    temp.pop()

        ans = []
        candidates.sort()
        backtrack([], 0, len(candidates), target)
        return ans
