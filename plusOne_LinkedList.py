# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        def DFS(head):
            if head == None:
                return 1
            carry = DFS(head.next)
            if carry == 0:
                return 0
            val = head.val + carry
            head.val = val%10
            return val/10
                
        if DFS(head) == 0:
            return head
        else:
            newHead = ListNode(1)
            newHead.next = head
            return newHead
        
        
        