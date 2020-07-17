# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """

        ans = list()
        s = list()
        while head:
            while s and s[-1][0] <head.val:
                _, t = s.pop()
                ans[t] = head.val
            s.append((head.val, len(ans)))
            ans.append(0)
            head = head.next
        return ans

        
