# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L1_s = ""
        L2_s = ""
        while l1:
            L1_s += str(l1.val)
            l1 = l1.next
        while l2:
            L2_s += str(l2.val)
            l2 = l2.next
        L =  str(int(L1_s)+int(L2_s))
        ans = ListNode(int(L[0]), None)
        curr = ans
        for i in range(1, len(L)):
            New = ListNode(int(L[i]), None)
            curr.next = New
            curr = curr.next
        return ans
