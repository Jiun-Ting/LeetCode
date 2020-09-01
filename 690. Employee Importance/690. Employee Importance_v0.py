"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        def DFS(i):
            ans = score[i]
            for j in sub[i]:
                ans += DFS(j)
            return ans
        score = collections.defaultdict(int)
        sub = collections.defaultdict(list)
        for employee in employees:
            score[employee.id] = employee.importance
            sub[employee.id] = employee.subordinates


        return DFS(id)
