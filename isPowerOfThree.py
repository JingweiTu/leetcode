class Solution(object):

    # Naive recursive solution.
    # O(n/3) == O(n) time complexity. Linear space complexity.
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # print(n)
        if n == 1:
            return True
            
        if n >= 3 and n%3 == 0:
            return self.isPowerOfThree(n/3)
            
        return False
