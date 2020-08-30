class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        Pass = [False]*len(rooms)
        q = collections.deque([0])
        Pass[0] = True
        while q:
            v = q.popleft()
            for i in rooms[v]:
                if Pass[i] == False:
                    Pass[i] = True
                    q.append(i)
        return sum(Pass)==len(rooms)
