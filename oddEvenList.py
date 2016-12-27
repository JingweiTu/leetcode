class Solution(object):

    # This doesn't work! Why? Think about pointers.
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        odd = head
        firstEven = head.next
        even = head.next
        node = firstEven
        i = 0
        while node:
            if i == 0:
                odd.next = node
                odd = node
                node = node.next
                i = 1
            else:
                even.next = node
                even = node.next
                node = node.next
                i = 0
        odd.next = firstEven
        return head

    