class Solution(object):

    # O(n/2) time complexity. Linear runtime.
    # Same concept as isPowerOfThree
    # Base case. n == 1. Return True. We know that all powers of 2 divided by 2 enough times
    # will ultimately result in 1.
    # Otherwise, as long as n is greater than 2 and divides evenly into 2, we continue.
    # Otherwise, we return False.
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n >= 2 and n%2 == 0:
            return self.isPowerOfTwo(n/2)
        else:
            return False
