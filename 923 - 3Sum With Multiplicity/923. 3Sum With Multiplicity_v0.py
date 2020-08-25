class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        A.sort()
        n = len(A)
        Mod = 10**9 + 7
        ans = 0
        for L in range(n-2):
            l, r = L+1, n-1
            while l < r:
                if A[L]+A[l] > target:
                    break
                total = A[L]+A[l]+A[r]
                if total == target:
                    lRepeat = 1
                    rRepeat = 1
                    if A[l]==A[r]:
                        ans += (r-l+1)*(r-l)/2
                        ans %= Mod
                        break
                    else:
                        while l < r and A[l] == A[l+1]:
                            l += 1
                            lRepeat += 1
                        while l < r and A[r] == A[r-1]:
                            r -= 1
                            rRepeat += 1
                        ans += lRepeat*rRepeat
                        ans %= Mod

                    r -= 1
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    l += 1

        return ans%Mod
