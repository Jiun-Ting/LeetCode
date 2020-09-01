class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        Trust = [0]*(N+1)
        Trusted = [0]*(N+1)
        for i in trust:
            print(i)
            Trust[i[0]] += 1
            Trusted[i[1]] += 1

        for i in range(1, N+1):
            if Trust[i] == 0 and Trusted[i] == N-1:
                return i
        return -1
        
