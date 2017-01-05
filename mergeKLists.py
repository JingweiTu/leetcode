# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import bisect
class Solution(object):

    # O(n^3) time complexity. Linear space complexity.
    # Cycle through each linked list within lists and use bisect's insertion sort function
    # to insert each val into the output list.
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        output = []
        for node in lists:
            while node != None:
                bisect.insort(output,node.val)
                node = node.next
        return output
