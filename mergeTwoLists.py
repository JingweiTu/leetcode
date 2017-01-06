# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import bisect

class Solution(object):

    # O(n) time complexity. Linear space complexity.
    # Simply travel through each linked list and insort each val into output.
    # insort() ensures that output is presorted.
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output = []
        node = l1
        while node != None:
            bisect.insort(output,node.val)
            node = node.next
        
        node = l2
        while node != None:
            bisect.insort(output,node.val)
            node = node.next
        
        return output
            
        