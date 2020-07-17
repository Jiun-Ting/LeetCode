# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        Input = head
        index = 0
        while (head.next != None):
            index += 1
            head = head.next

        Index = index/2
        if (index%2 ==0):
            while (Index > 0):
                Input = Input.next
                Index -= 1
        else:
            while (Index >= 0):
                Input = Input.next
                Index -= 1
        return Input

        
