# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        Next = head.next
        head.next = None
        while (Next != None):
            temp = head
            head = Next
            Next = head.next
            head.next = temp
        return head
