class Solution(object):

    # O(n) solution. Linear space complexity. 
    # Set a toggle such that we increment our count only if we hit a non-space char and 
    # that there was a space char before that non-space char.
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        toggle = 1
        for i in s:
            if not i == " " and toggle:
                count += 1
                toggle = 0
            if i == " ":
                toggle = 1
        return count
        