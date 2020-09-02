class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        def DFS(k, account):
            v[k] = True
            account.append(k)
            for i in Map[k]:
                for j in accounts[i][1:]:
                    if v[j] == False:
                        account = DFS(j, account)
            return account

        Map = collections.defaultdict(list)
        v = collections.defaultdict(bool)
        for i, L in enumerate(accounts):
            for m in L[1:]:
                Map[m].append(i)
                v[m] = False
        ans = []
        for k in Map.keys():
            if v[k] == False:
                name = accounts[Map[k][0]][0]
                account = DFS(k, [])
                ans.append([name] + sorted(account))
        return ans
